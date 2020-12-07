from rest_framework.serializers import ModelSerializer

from .models import Locode


class LocodeSerializer(ModelSerializer):
    class Meta:
        model = Locode
        fields = '__all__'
