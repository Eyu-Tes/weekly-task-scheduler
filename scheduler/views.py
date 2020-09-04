from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import UserRegistrationForm, UserLoginForm, TaskFormSet
from .models import Task


# Create your views here.
def sign_up(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context=context)


def sign_in(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('user_home', pk=user.id, day='monday')
            else:
                messages.error(request, 'Username or password is incorrect')
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context=context)


@login_required
def task_scheduler_view(request, pk, day):
    user_obj = User.objects.get(id=pk)
    if request.method == 'POST':
        task_formset = TaskFormSet(request.POST, instance=user_obj, initial=[{'day': day}],
                                   queryset=Task.objects.filter(day=day))
        if task_formset.is_valid():
            task_formset.save()
            return redirect('user_home', pk=user_obj.id, day=day)
    else:
        task_formset = TaskFormSet(instance=user_obj, initial=[{'day': day}],
                                   queryset=Task.objects.filter(day=day))
    context = {
        'formset': task_formset,
    }
    return render(request, 'scheduler/task_scheduler.html', context=context)
