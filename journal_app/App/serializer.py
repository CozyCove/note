from rest_framework import serializers
from .models import note


class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = note
    fields = ['text','created_at']