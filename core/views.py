from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.exceptions import NotFound

from core.models import Avtomobil
from core.serializer import AvtomobilSerializer


# Create your views here.
class AvtomobilListCreateView(APIView):
    def get(self, request):
        avtomobillar = Avtomobil.objects.all()
        serializer = AvtomobilSerializer(avtomobillar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvtomobilSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        avtomobil = Avtomobil.objects.create(**serializer.validated_data)
        s = AvtomobilSerializer(avtomobil)
        return Response(s.data, status=201)


class AvtomobilDetailView(APIView):
    def get(self, request, id):
        try:
            avtomobil = Avtomobil.objects.get(id=id)
        except Avtomobil.DoesNotExist:
            NotFound("Avtomobil topilmadi")
        serializer = AvtomobilSerializer(avtomobil)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            avtomobil = Avtomobil.objects.get(id=id)
        except Avtomobil.DoesNotExist:
            NotFound("Avtomobil topilmadi")
        serializer = AvtomobilSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        avtomobil.modeli = serializer.validated_data["modeli"]
        avtomobil.markasi = serializer.validated_data["markasi"]
        avtomobil.narxi = serializer.validated_data["narxi"]
        avtomobil.ishlab_chiqarilgan_yili = serializer.validated_data["ishlab_chiqarilgan_yili"]
        avtomobil.yurgan_masofasi = serializer.validated_data["yurgan_masofasi"]
        avtomobil.yoqilgi_turi = serializer.validated_data["yoqilgi_turi"]
        avtomobil.izohi = serializer.validated_data["izohi"]
        avtomobil.save()
        s = AvtomobilSerializer(avtomobil)
        return Response(s.data)

    def delete(self, request, id):
        try:
            avtomobil = Avtomobil.objects.get(id=id)
        except Avtomobil.DoesNotExist:
            NotFound("Avtomobil topilmadi")
        avtomobil.delete()
        return Response(status=204)
