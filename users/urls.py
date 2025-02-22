from django.urls import path
from .views import CreateUser

urlpatterns = [
    path('sign-up/', CreateUser.as_view(), name="sign_up")
]