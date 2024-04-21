from django.urls import path
from . import views
urlpatterns = [
    path('', views.write),
    path('write', views.write),
    path('notes', views.notes),
]
