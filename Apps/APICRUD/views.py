from rest_framework import viewsets

from Apps.APICRUD.models import CatalogoModelo
from Apps.APICRUD.serializers import CatalogoSerialize

class CatalogoView(viewsets.ModelViewSet):
    queryset = CatalogoModelo.objects.all()
    serializer_class = CatalogoSerialize