from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import UserRegistrationForm, UserLoginForm, TaskForm
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


def task_scheduler_view(request, pk, day):
    tasks = Task.objects.filter(user_id=pk, day=day)
    task_form = TaskForm(request.POST or None,
                         initial={'user': get_object_or_404(User, id=pk), 'day': day})

    context = {'tasks': tasks, 'task_form': task_form}
    return render(request, 'scheduler/task_scheduler.html', context=context)


class CreateTaskView(View):
    def get(self, request):
        task_name = request.GET.get('task_name', None)
        start_time = request.GET.get('start_time', None)
        end_time = request.GET.get('end_time', None)
        day = request.GET.get('day', None)
        user = self.request.user

        obj = Task.objects.create(
            user=user,
            day=day,
            task_name=task_name,
            start_time=start_time,
            end_time=end_time,
        )

        task = {'id': obj.id, 'task_name': obj.task_name, 'start_time': obj.start_time, 'end_time': obj.end_time}

        data = {'task': task}
        return JsonResponse(data)


class UpdateTaskView(View):
    def get(self, request):
        task_id = request.GET.get('task_id', None)
        task_name = request.GET.get('task_name', None)
        start_time = request.GET.get('start_time', None)
        end_time = request.GET.get('end_time', None)
        # day = request.GET.get('day', None)
        # user = self.request.user

        obj = Task.objects.get(id=task_id)
        obj.task_name = task_name
        obj.start_time = start_time
        obj.end_time = end_time
        obj.save()

        task = {'id': obj.id, 'task_name': obj.task_name, 'start_time': obj.start_time, 'end_time': obj.end_time}
        data = {'task': task}
        return JsonResponse(data)


class DeleteTaskView(View):
    def get(self, request):
        task_id = request.GET.get('task_id', None)
        Task.objects.get(id=task_id).delete()
        data = {'deleted': True}
        return JsonResponse(data)
