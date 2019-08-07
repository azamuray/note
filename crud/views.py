from django.shortcuts import render
from django.views.generic import ListView

from .models import Note


class NoteListView(ListView):
	model = Note