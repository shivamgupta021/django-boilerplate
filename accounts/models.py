from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars/", null=True, blank=True)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.display_name is not None:
            return self.display_name
        else:
            return self.user.username

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        else:
            return static("images/avatar.svg")
