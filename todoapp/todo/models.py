from django.db import models

import uuid

# Create your models here.

class User (models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=130)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	registerDate = models.DateTimeField(auto_now=True)


	@classmethod
	def create (cls, email, password, firstname, lastname):
		user = cls(email=email, password=password, firstname=firstname, lastname=lastname)
		return user

	def __str__ (self):
		return str(self.uuid)

class Task (models.Model):
	userUUID = models.ForeignKey(User, on_delete=models.CASCADE)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=300)
	finishDate = models.DateTimeField('deadline date')
	finished = models.BooleanField(default=False)

	@classmethod
	def create (cls, title, finishDate, userUUID):
		task = cls(title=title, finishDate=finishDate, userUUID=userUUID)
		return task

	def __str__ (self):
		return self.title