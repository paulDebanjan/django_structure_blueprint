"""bloggingSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.urls import path, include,re_path
from django.views.static import serve
from django.contrib import admin
from django.conf import settings

from .views import decision,document_print

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',decision, name="decision"),
    path('doc',name="document",view=document_print),
    path("user/",include("bloggingSite.user.urls")),
    path("newsFeed/",include("bloggingSite.newsFeed.urls")),
    path("administration/",include("bloggingSite.administration.urls")),
    path("accounts/",include("bloggingSite.authentication.urls")),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),name='password_reset_complete'),
    #Debug Fase Mode
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
# handler500 = error500.as_view()
# For Media
if settings.DEBUG:
        urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
