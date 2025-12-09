from django.urls import path
from .views import UserRegisterView,logged_out_view,logout_view

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('logout/',logout_view,name='logout'),
    path('logged-out/',logged_out_view,name='logged-out'),
]