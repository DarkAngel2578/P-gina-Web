from django.urls import path

from AppPrimaria import views

urlpatterns = [
    
    path('', views.home),
    path('texto/', views.textos)
]

