from django.http import JsonResponse
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


class AjaxableResponseMixin:

	def form_invalid(self, form):
		response = super().form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		else:
			return response

	def form_valid(self, form):
		form.instance.creator = self.request.user
		response = super().form_valid(form)
		if self.request.is_ajax():
			data = {
				'pk': self.object.pk,
			}
			return JsonResponse(data)
		else:
			return response


class NoteCreateView(AjaxableResponseMixin, LoginRequiredMixin, CreateView):
	model = Note
	fields = ['title', 'body']
	login_url = 'crud:note-list'