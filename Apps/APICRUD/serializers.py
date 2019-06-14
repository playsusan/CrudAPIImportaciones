from rest_framework import serializers
from Apps.APICRUD.models import CatalogoModelo

class CatalogoSerialize(serializers.ModelSerializer):
    class Meta:
        model = CatalogoModelo
        fields = ['pk','codigo', 'nombre', 'detalle', 'precio', 'fecha', 'stock']