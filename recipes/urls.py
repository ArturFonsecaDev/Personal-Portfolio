from django.urls import path
from recipes.views import home_page, processing_forms

urlpatterns = [
    path('', home_page),
    path('contact/', processing_forms, name='processing_forms'),
]
