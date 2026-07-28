from django.urls import path

from core import views

urlpatterns = [
    path(
        "api/avtomobillar",
        views.AvtomobilListCreateView.as_view(),
        name="avtomobillar",
    ),
    path(
        "api/avtomobillar/<id>",
        views.AvtomobilDetailView.as_view(),
        name="avtomobillar",
    ),
]
