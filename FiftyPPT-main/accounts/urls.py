# users/urls.py
from django.urls import path
from .views import RegisterView, register, SigninView, Signin, logout_view

urlpatterns = [
    # path('register/', RegisterView.as_view()),

    path('signin/', Signin.as_view(), name='signin'),
    path('api/signin/', SigninView.as_view()),

    path('signup/', register, name='register'),
    path('api/signup/', RegisterView.as_view()),

    path('logout/', logout_view, name='logout'),
]
