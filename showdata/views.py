from rest_framework import viewsets, mixins ,status
from .serializers import ShowDataSerializer
from .models import ShowData

class ShowDataViewSet(viewsets.ModelViewSet):
    serializer_class = ShowDataSerializer
    queryset = ShowData.objects.all()

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)