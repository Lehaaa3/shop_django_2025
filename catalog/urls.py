from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import main, contact, catalog, category

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('catalog/', catalog, name='catalog'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
]
