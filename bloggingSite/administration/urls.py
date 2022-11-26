from django.urls import reverse, reverse_lazy
from django.urls import path
from .views import UserListView

app_name = "administration"
urlpatterns=[
    path(
        route='home/',
        view=UserListView.as_view(),
        name='home'
    ),
]