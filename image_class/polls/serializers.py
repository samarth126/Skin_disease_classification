from dataclasses import fields
from rest_framework import serializers
from .models import *


class Dataset_name(serializers.ModelSerializer):
    class Meta:
        model= Dataset
        fields='__all__'

# class classification_request(serializers.Serializer):
#    img = fields.ImageField()

class Image_req_serealize(serializers.Serializer):
    # email = serializers.EmailField()
    image = serializers.ImageField()
    # content = serializers.CharField(max_length=200)