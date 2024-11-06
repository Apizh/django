from django.urls import path
from . import views
urlpatterns = [
    path('', views.method),
    path('about', views.method1),
]