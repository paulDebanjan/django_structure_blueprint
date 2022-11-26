from django.shortcuts import render,redirect
from .models import NewsFeedImagesModel, NewsFeedMessageModel
import uuid 

def CreateNewsFeedView(request):
    if request.method == "POST":
        newsFeed_id = uuid.uuid4()
        images = request.FILES.getlist('images')
        messages = request.POST["message"]
        NewsFeedMessageModel.objects.create(message=messages, creator = request.user, newsFeedID = newsFeed_id)
        for image in images:
            NewsFeedImagesModel.objects.create(images = image, creator = request.user, newsFeedID = newsFeed_id)
        return redirect("user:news_feed")
    return render(request, "newsFeed/create_news_feed_view.html")
