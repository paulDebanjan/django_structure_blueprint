from django.shortcuts import render,redirect

def decision(request):
    if not request.user.is_authenticated:
        return redirect("authentication:login")
    if request.user.is_user:
        return redirect("user:news_feed")
    elif request.user.is_administrator:
        return redirect("administration:home")
    else:
        pass
    return render(request,'decision.html')