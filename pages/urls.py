from django.urls import path
from .views import HomePageView, AboutView


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]