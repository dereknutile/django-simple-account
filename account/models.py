from django.db import models
from django.contrib.auth.models import User
        

class UserProfile(models.Model):
    # Link the UserProfile to the Django User model.
    user = models.OneToOneField(User)

    # Extended attributes
    accepted_nda = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

