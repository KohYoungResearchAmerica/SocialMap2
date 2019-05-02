from django.urls import path, re_path

from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('<int:user_id>/result/', views.result, name='result'),
]
