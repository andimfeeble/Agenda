from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='list'),
    path('<slug:pk>/', views.ContatoDetailView.as_view(), name='detail'),
]
