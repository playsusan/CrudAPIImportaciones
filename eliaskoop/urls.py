from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('Apps.APICRUD.urls')),
    path('vista/', include('Apps.CONSUMOAPI.urls')),
]
