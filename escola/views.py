from rest_framework import viewsets
from escola.models import ALuno
from escola.serializer import ALunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = ALuno.objects.all()
    serializer_class = ALunoSerializer
