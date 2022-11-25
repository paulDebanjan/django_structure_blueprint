from django.shortcuts import render


def newsFeedView(request):
    return render(request,"user/news_feed.html")