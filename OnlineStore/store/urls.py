import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='index'),
]