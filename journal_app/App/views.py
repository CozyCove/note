from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import note
from .serializer import NoteSerializer
from .forms import NoteForm


def write(request):
  if request.method == 'POST':
    form = NoteForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request,"App/notes.html")
    else:
      return render(request,"App/write.html",{"error":"tarung na"})
  return render(request,"App/write.html")

def notes(request):
  notes = note.objects.all().order_by('-created_at')
  serialized = NoteSerializer(notes,many=True)
  return JsonResponse({"notes":serialized.data})
# Create your views here.
