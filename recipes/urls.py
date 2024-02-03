from django.urls import path
from recipes.views import home, contato, sobre

# dominio/recipes/sobre

urlpatterns = [
    path('', home),  # /
    path('sobre/', sobre),  # sobre/
    path('contato/', contato),  # contato/
]
