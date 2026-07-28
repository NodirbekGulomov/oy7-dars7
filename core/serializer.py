from rest_framework import serializers


class AvtomobilSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    modeli = serializers.CharField(max_length=100)
    markasi = serializers.CharField(max_length=100)
    narxi = serializers.DecimalField(max_digits=20, decimal_places=2)
    ishlab_chiqarilgan_yili = serializers.IntegerField()
    yurgan_masofasi = serializers.IntegerField()
    yoqilgi_turi = serializers.CharField(max_length=50)
    izohi = serializers.CharField()
