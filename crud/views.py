from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView
)

from .models import Note


class NoteListView(ListView):
	model = Note


class NoteDetailView(DetailView):
	model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
	model = Note
	fields = ['title', 'body']
	login_url = 'crud:note-list'

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)