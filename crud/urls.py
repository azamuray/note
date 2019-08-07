from django.urls import path

from .views import NoteListView, NoteDetailView

app_name = 'crud'
urlpatterns = [
	path('', NoteListView.as_view(), name='note-list'),
	path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]