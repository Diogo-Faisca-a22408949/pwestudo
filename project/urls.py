from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

# Inicializa a instância da API
api = NinjaAPI()

# Adiciona o router da tua app 'pessoas' à API principal

urlpatterns = [
    path('admin/', admin.site.urls),
    # Expõe a API no caminho /api/
    path('api/', api.urls),
]