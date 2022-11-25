from django.shortcuts import render
from .models import NewsFeedModel

def CreateNewsFeedView(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        # messages = request.POST("message")
        # print(messages)
        # NewsFeedModel.create(message = message)
        for image in images:
            NewsFeedModel.objects.create(images = image)
    return render(request, "newsFeed/create_news_feed_view.html")
