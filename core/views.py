# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from core.models import Avtomobil, IshlabChiqaruvchi
from core.serializer import (
    AvtomobilDetailSerializer,
    AvtomobilListSerializer,
    AvtomobilSerializer,
    IshlabChiqaruvchiSerializer,
)


# Create your views here.
class AvtomobilPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20


class IshlabChiqaruvchiListCreateView(ListCreateAPIView):
    queryset = IshlabChiqaruvchi.objects.all()
    serializer_class = IshlabChiqaruvchiSerializer


class AvtomobilListCreateView(ListCreateAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer
    pagination_class = AvtomobilPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AvtomobilListSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(yaratuvchi="Sanjarbek")


class IshlabChiqaruvchiDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = IshlabChiqaruvchi.objects.all()
    serializer_class = IshlabChiqaruvchiSerializer


class AvtomobilDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer
    lookup_field = "kod"
    lookup_url_kwarg = "kod"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return AvtomobilSerializer
        return AvtomobilDetailSerializer

    def perform_update(self, serializer):
        serializer.save(oxirgi_tahrirlagan="Akmal")

    def get_queryset(self):
        queryset = super().get_queryset()
        marka = self.request.query_params.get("marka")
        min_narx = self.request.query_params.get("min_narx")
        max_narx = self.request.query_params.get("max_narx")
        yil = self.request.query_params.get("ishlab_chiqarilgan_yili")

        if marka:
            queryset = queryset.filter(marka=marka)
        if min_narx:
            queryset = queryset.filter(narx__gte=min_narx)
        if max_narx:
            queryset = queryset.filter(narx__lte=max_narx)
        if yil:
            queryset = queryset.filter(ishlab_chiqarilgan_yili=yil)

        return queryset
