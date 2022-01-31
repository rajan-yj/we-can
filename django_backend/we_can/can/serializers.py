from .models import Can
from rest_framework import serializers


class CanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Can
        fields = "__all__"