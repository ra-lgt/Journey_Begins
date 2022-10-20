from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('signout',views.signout),
    path('register',views.register),

]