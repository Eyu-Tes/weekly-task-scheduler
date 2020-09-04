from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Task


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'}), label='Password')
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Retype password'}), label='Confirm password')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'}))


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['task_name', 'start_time', 'end_time', 'day']
#
#         widgets = {
#             'task_name': forms.TextInput(attrs={'class': 'form-control form-control-sm',
#                                                 'placeholder': 'task name'}),
#             'start_time': forms.TimeInput(attrs={'class': 'form-control form-control-sm',
#                                                  'type': 'time', 'placeholder': 'start'}),
#             'end_time': forms.TimeInput(attrs={'class': 'form-control form-control-sm',
#                                                'type': 'time'}),
#             'day': forms.HiddenInput(),
#         }


TaskFormSet = forms.inlineformset_factory(
    User,
    Task,
    fields=['task_name', 'start_time', 'end_time'],
    extra=1,
    widgets={
        'task_name': forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                            'placeholder': 'task name'}),
        'start_time': forms.TimeInput(attrs={'class': 'form-control form-control-sm',
                                             'type': 'time', 'placeholder': 'start'}),
        'end_time': forms.TimeInput(attrs={'class': 'form-control form-control-sm',
                                           'type': 'time'}),
    }
)
