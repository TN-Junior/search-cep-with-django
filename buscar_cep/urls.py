from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Faz a raiz carregar a view `index`
    path('index/', views.index, name='index'),
    path('consulta_api/', views.consulta_api, name='consulta_api'),
]
