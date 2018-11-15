from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name="index"),
    # path('about/', views.AboutView.as_view())
]
