from django.urls import path
from .views import home, about_us, contact_us

urlpatterns = [
    path('home/', home, name="home"),
    path('about/', about_us, name="about"),
    path('contact/', contact_us, name="contact"),
]
