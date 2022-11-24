from django.shortcuts import render
from .forms import UserSignUpForm
from .models import User


class userSignUpView(CreateView):
    model=User
    form_class=UserSignUpForm
    template_name = 'authentication/form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

