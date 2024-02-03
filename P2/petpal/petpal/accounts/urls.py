# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('shelter/list', ShelterListView.as_view(), name='shelter-list'),
    path('seeker/<str:username>', SeekerProfileUpdateDeleteView.as_view(), name='seeker-all'),
    path('shelter/<str:username>', ShelterProfileUpdateDeleteView.as_view(), name='shelter-all'),


    # Add other views as needed
]
