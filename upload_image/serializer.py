from rest_framework import serializers
import time
from .models import UploadImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'

    def validate(self, data):
        if data['image'].size > 200000:
            raise serializers.ValidationError("size > 20kB")
        data['image'].name = ''.join([str(time.time()), '_', data['image'].name])
        return data