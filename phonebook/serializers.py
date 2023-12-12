from rest_framework import serializers
from . import models


class PersoneSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        name = validated_data.get('name')
        return models.Persone.objects.create(name=name)
    
    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        instance.name = name
        instance.save()

        return instance

