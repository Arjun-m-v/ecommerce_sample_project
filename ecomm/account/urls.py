from django.urls import path
from account.views import *

urlpatterns = [
    path('login',LoginView.as_view(),name="login"),
    path('reg',RegisterView.as_view(),name="reg"),
    path('logout',LogoutView.as_view(),name="logout"),
]