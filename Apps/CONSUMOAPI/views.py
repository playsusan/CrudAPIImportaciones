from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.views import APIView

from Apps.APICRUD.models import CatalogoModelo
from Apps.APICRUD.serializers import CatalogoSerialize

class catalogoAPI(APIView):
    serializer = CatalogoSerialize

    def get(self, request, format=None):
        datos = CatalogoModelo.objects.all()
        response = self.serializer(datos, many=True)
        salida = json.dumps(response.data)
        return HttpResponse(salida, content_type='application/json')

        

