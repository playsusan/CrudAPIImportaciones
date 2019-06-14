from django.urls import path, include

from Apps.CONSUMOAPI.views import *

urlpatterns= [
	path('', catalogoAPI.as_view(), name="catalogoAPI"),
]