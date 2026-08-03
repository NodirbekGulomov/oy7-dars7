from django.urls import path

from core import views

urlpatterns = [
    path("ishlab-chiqaruvchi", views.IshlabChiqaruvchiListCreateView.as_view()),
    path("avtomobil", views.AvtomobilListCreateView.as_view()),
    path("ishlab-chiqaruvchi/<int:pk>", views.IshlabChiqaruvchiDetailApiView.as_view()),
    path("avtomobil/<slug:kod>", views.AvtomobilDetailApiView.as_view()),
]
