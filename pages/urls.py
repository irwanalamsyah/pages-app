from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about_url'),
    path('', HomePageView.as_view(), name='home_url'),
]
