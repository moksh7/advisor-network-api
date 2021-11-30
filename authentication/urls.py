from django.urls import path
from authentication import views

urlpatterns = [
    path('user/register/',views.RegisterView.as_view(),name='register'),
    path('register/admin/',views.RegisterAdmin.as_view(),name='adminregister'),
    path('user/login/',views.LoginView.as_view(),name='login'),
    path('users/',views.Allusers.as_view(),name='all'),
]
