from django.urls import path

from .views import (
	NoteListView,
	NoteDetailView,
	NoteCreateView
)

app_name = 'crud'
urlpatterns = [
	path('', NoteListView.as_view(), name='note-list'),
	path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
	path('create/', NoteCreateView.as_view(), name='note-create'),
]