from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Todo


class Command(BaseCommand):
	def handle(self, *args, **options):
		try:
			todos = Todo.objects.all()
			for todo in todos:
				if todo.send_email:
					if todo.when_to_send > timezone.now():
						# if timezone.now() == todo.when_to_send:
						send_mail(
							'your todo {0} time is now'.format(todo.title),
							'now its time for your todo "{0}" and you available sending email notification. you can find it here : {1}'.format(todo.title, "http://127.0.0.1:8000/api/v1/todo/{0}".format(todo.key)),
							'winmicro7farantgh@gmail.com',
							[todo.user.email],
							fail_silently=False,
							)
						self.stdout.write(self.style.SUCCESS("email sent to '%s'"% todo.user.username))
		except Exception as e:
			self.stdout.write(e)
