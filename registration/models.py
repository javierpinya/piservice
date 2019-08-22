from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def custom_upload_to(instance, filename):
	old_instance = Profile.objects.get(pk=instance.pk)
	old_instance.avatar.delete()
	return 'profiles/' + filename

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#vatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
	avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	link = models.URLField(max_length=200, null=True, blank=True)