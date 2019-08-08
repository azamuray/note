from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Note(models.Model):
	title 	= models.CharField("Название", max_length=120)
	body 	= models.TextField("Описание")
	creator = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('crud:note-detail', kwargs={'pk': self.pk})