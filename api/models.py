from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random
import string


def todo_image(instance, filename):
	return "todo/{0}/{1}.jpg".format(instance.user.username, instance.title)


def user_image(instance, filename):
	date_time = datetime.now().strftime("%Y_%m_%d-%H%M%S")
	saved_file_name = instance.user.username + "-" + date_time + ".jpg"
	return "profile/{0}/{1}".format(instance.user.username, saved_file_name)


def random_key():
	allowed_chars = list(string.ascii_lowercase) + list(string.digits)
	random_key = ""
	key = random_key.join(random.sample(allowed_chars, 15))
	return key


class Todo(models.Model):
	PRIORITY_CHOICES = [
		('high', "High"),
		('medium', "Medium"),
		('low', "Low"),
	]
	key = models.CharField(
		max_length=15, default=random_key, unique=True, blank=False, null=False
	)

	title = models.CharField(max_length=500, null=False, blank=False)
	description = models.TextField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(
		upload_to=todo_image, default='todo/default/default.jpg'
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True, blank=False, null=False)
	priority = models.CharField(
		max_length=6, choices=PRIORITY_CHOICES, default='medium'
	)

	send_email = models.BooleanField(default=False)
	is_paused = models.BooleanField(blank=False, null=False)
	is_visible = models.BooleanField(blank=False, null=False)
	date = models.CharField(max_length=50, blank=False, null=False)
	time = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.title


class Profile(models.Model):
	key = models.CharField(
		max_length=15, default=random_key, unique=True, blank=False, null=False
	)

	user = models.OneToOneField(
		User, on_delete=models.CASCADE, related_name='profile'
	)

	image = models.ImageField(
		upload_to=user_image, default="profile/default/default.jpg"
	)

	def __str__(self):
		return self.user.username


class Contact(models.Model):
	name = models.CharField(max_length=20, null=False, blank=False)
	email = models.EmailField()
	text = models.TextField()

	def __str__(self):
		return self.name
