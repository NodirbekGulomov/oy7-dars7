from rest_framework import serializers

from core.models import Avtomobil


class AvtomobilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtomobil
        fields = [
            "id",
            "modeli",
            "markasi",
            "narxi",
            "ishlab_chiqarilgan_yili",
            "yurgan_masofasi",
            "yoqilgi_turi",
            "izohi",
            "yaratilgan_vaqti",
        ]

        read_only_fields = [
            "id",
            "yaratilgan_vaqti",
        ]

    def validate_modeli(self, modeli: str):
        sozlar = ["test", "semo", "sample"]
        for soz in sozlar:
            if modeli.lower().startswith(soz):
                raise serializers.ValidationError(
                    "Avtomobil modeli Test, Demo yoki Sample bilan boshlanishi mumkin emas."
                )
        return modeli

    def validate_markasi(self, markasi: str):
        markalar = ["chevrolet", "kia", "hyundai", "toyota", "bmw"]
        if markasi not in markalar:
            raise serializers.ValidationError(f"Faqat {markalar} bolishi kerak.")
        return markasi

    def validate_narxi(self, narxi):
        if str(narxi).split(".")[0].endswith("999"):
            raise serializers.ValidationError("Narxi 999 bilan tugamasligi kerak.")
        return narxi

    def validate(self, data: dict):
        ishlab_chiqarilgan_yili = data.get("ishlab_chiqarilgan_yili")
        yurgan_masofasi = data.get("yurgan_masofasi")
        narxi = data.get("narxi")
        markasi = data.get("markasi")

        if (
            ishlab_chiqarilgan_yili
            and yurgan_masofasi
            and ishlab_chiqarilgan_yili >= 2024
            and yurgan_masofasi > 50_000
        ):
            raise serializers.ValidationError(
                "Ishlab chiqarilgan yili 2024 yoki undan keyin bo'lsa "
                "yurgan masofasi 50 000 km dan oshmasligi kerak."
            )

        if (
            narxi
            and ishlab_chiqarilgan_yili
            and narxi > 100_000
            and ishlab_chiqarilgan_yili < 2005
        ):
            raise serializers.ValidationError(
                "Narxi 100 000 dan yuqori bo'lsa "
                "avtomobil 2005-yildan eski bo'lishi mumkin emas."
            )

        if markasi and narxi and markasi.lower() == "bmw" and narxi < 30_000:
            raise serializers.ValidationError(
                "Markasi BMW bo'lsa narxi kamida 30 000 bo'lishi kerak"
            )
        return data


class AvtomobilListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtomobil
        fields = ["id", "modeli", "markasi", "narxi"]


class AvtomobilCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtomobil
        exclude = ["id", "izohi", "yaratilgan_vaqti"]
