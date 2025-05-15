from django.shortcuts import render

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, note_id):
    note = Notes.objects.get(id=note_id)
    return render(request, 'notes/notes_detail.html', {'note': note})
#     def __str__(self):