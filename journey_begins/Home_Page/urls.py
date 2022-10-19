from . import views
from django.urls import path

urlpatterns = [
    path('',views.Sign_in_Sign_up.home),

    path('register',views.Sign_in_Sign_up.register)
]