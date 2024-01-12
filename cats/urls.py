# urls.py
from django.urls import path
from .views import CatListCreateView, CatRetrieveUpdateDestroyView

urlpatterns = [
    path('', CatListCreateView.as_view(), name='cat-list-create'),
    path('<int:pk>/', CatRetrieveUpdateDestroyView.as_view(), name='cat-retrieve-update-destroy'),
]
