from rest_framework import serializers


class AvtomobilSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    modeli = serializers.CharField(min_length=2, max_length=100)
    markasi = serializers.CharField(max_length=30)
    narxi = serializers.DecimalField(
        max_digits=20, decimal_places=2, min_value=1000, max_value=1000000
    )
    ishlab_chiqarilgan_yili = serializers.IntegerField(min_value=1990, max_value=2026)
    yurgan_masofasi = serializers.IntegerField(min_value=0, max_value=1000000)
    yoqilgi_turi = serializers.CharField(max_length=20)
    izohi = serializers.CharField(write_only=True, required=False, allow_blank=True)
    yaratilgan_vaqti = serializers.DateTimeField(read_only=True)

    
