from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
@receiver(post_save, sender=User)
class Profile(models.Model):
    choice_field = [('h', 'Hulk'),
                    ('t', 'Thor'),
                    ('c', 'Captain America'),
                    ('i', 'Iron Man')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=7500)
    rank = models.IntegerField(default=0)
    profile_type = models.CharField(choices=choice_field, default='t', max_length=100)

    def css_class(self):
        if self.profile_type == 't':
            return 'warning'
        elif self.profile_type == 'h':
            return 'success'
        elif self.profile_type == 'c':
            return 'primary'
        elif self.profile_type == 'i':
            return 'danger'
        else:
            return 'secondary'

    def __str__(self):
        return self.user.username
