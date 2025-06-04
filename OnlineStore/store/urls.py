import views
from django.urls import path

urlpatterns = [
    path('', views.StoreView.as_view(), name='index'),
]