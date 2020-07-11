from django.db.models.signals import post_save
from django.contrib.auth.models import User #sender=User
from django.dispatch import receiver
from users.models import Profile # receiver

@receiver(post_save,sender=User)
def create_profile(sender,created,instance,*args,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,*args,**kwargs):
	return instance.profile.save()

