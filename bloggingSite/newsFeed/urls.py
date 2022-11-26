from django.urls import path
from .views import CreateNewsFeedView

app_name = "newsFeed"
urlpatterns = [
    path(
        route='create/',
        view=CreateNewsFeedView,
        name='create'
    ),
]