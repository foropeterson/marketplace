from django.urls import path
from .views import profile_view

urlpatterns = [
    # Other URL patterns...
    path('accounts/profile/', profile_view, name='profile'),
]