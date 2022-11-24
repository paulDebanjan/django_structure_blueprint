from django.shortcuts import render

def postView(request):
    return render(request, "social_media/home.html")