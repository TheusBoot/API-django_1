from rest_framework import serializers
from escola.models import ALuno

class ALunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALuno
        Fields = ['id','nome','rg']
