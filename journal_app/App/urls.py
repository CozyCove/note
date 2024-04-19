from django.urls import path
from . import views
urlpatterns = [
    path('see', views.home),
    path('write', views.write),
    path('notes', views.notes),
]
