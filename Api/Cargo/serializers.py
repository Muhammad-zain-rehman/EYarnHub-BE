from Api.Cargo.models import Cargo
from rest_framework import serializers


class CargoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    slogan = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    phone_number = serializers.CharField(required=True, allow_null=False, allow_blank=False)

    class Meta:
        model = Cargo
        fields = ['id', 'name', 'slogan', 'phone_number']

    def create(self, validated_data):
        cargo_company = Cargo.objects.create(**validated_data)
        cargo_company.save()

        return cargo_company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slogan = validated_data.get('slogan', instance.slogan)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance
