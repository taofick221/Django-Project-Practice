from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Post

@receiver(pre_save,sender=Post)
def before_post_save(sender,instance,**kwargs):
    print(f"About to save blog:{instance.title}")

@receiver(post_save,sender=Post)
def after_post_save(sender,instance,created,**kwargs):
    if created:
        print(f"New blog created:{instance.title}")
    else:
        print(f" blog update:{instance.title}")

