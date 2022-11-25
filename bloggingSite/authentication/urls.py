from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_view
from django.urls import path
from .views import userSignUpView

app_name = "authentication"
urlpatterns=[
    path(
        route='signup/',
        view=userSignUpView.as_view(),
        name='signup'
    ),
    path(
        route='login/',
        view=auth_view.LoginView.as_view(template_name='authentication/form.html', success_url="decision"),
        name='login'
    ),
    path(
        route='logout/',
        view=auth_view.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='password_change/',
        view=auth_view.PasswordChangeView.as_view(success_url=reverse_lazy('userAuthentication:password_change_done'),template_name='userAuthentication/password_change.html'),
        name='password_change'
    ),
    path(
        route='password_change/done/',
        view=auth_view.PasswordChangeDoneView.as_view(template_name='userAuthentication/password_change_done.html'),
        name='password_change_done'
    ),
    # path(
    #     route='password_reset/',
    #     view=classroom.ResetPasswordView.as_view(),
    #     name='password_reset'

    # ),
    path(
        route='password_reset/done',
        view=auth_view.PasswordResetDoneView.as_view(template_name='userAuthentication/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        route='reset/<uidb64>/<token>/',
        view=auth_view.PasswordResetConfirmView.as_view(template_name='userAuthentication/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        route='reset/done/',
        view=auth_view.PasswordResetCompleteView.as_view(template_name='userAuthentication/password_reset_done.html'),
        name='password_reset_complete'
    ),
]