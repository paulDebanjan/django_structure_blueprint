from django.urls import reverse, reverse_lazy
from django.urls import path
from .views import adminView

app_name = "administration"
urlpatterns=[
    path(
        route='home/',
        view=adminView,
        name='home'
    ),
]