from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import User


class userSignUpView(CreateView):
    model=User
    form_class=UserSignUpForm
    template_name = 'authentication/form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('decision')

