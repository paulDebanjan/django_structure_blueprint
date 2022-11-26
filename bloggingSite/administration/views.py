from django.shortcuts import render
from django.views.generic import ListView
from bloggingSite.authentication.models import User


class UserListView(ListView):
    model = User 
def adminView(request):
    return render(request,"administration/home.html")