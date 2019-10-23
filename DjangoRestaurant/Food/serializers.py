from rest_framework import serializers
from Food.models import Foods


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['name', 'price', 'picture', 'description']
