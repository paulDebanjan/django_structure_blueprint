from django.urls import path
from .views import newsFeedView
app_name = "user"

urlpatterns = [
    path(
        route='',
        view=newsFeedView,
        name='news_feed'
    ),
]