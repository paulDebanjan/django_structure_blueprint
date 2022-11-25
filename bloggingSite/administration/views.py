from django.shortcuts import render


def adminView(request):
    return render(request,"administration/home.html")