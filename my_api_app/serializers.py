from django.contrib.auth.models import Group
from rest_framework import serializers

from my_api_app.models import Product


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="pk","name"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="pk","name","description","price","discount","created_at","arhive","preview"


