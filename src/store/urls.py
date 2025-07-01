from store import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name='index'),
]