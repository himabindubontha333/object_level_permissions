from django.db import models
from django.contrib.auth.models import Permission,Group
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

class Object(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk:self.pk"})

    class Meta:
        permissions = [
            ("view_secure_object", "Can view the object"),
            ("change_secure_object", "Can change the object"),
            ("delete_secure_object", "Can delete the object"),
        ]

    def __str__(self):
        return self.name
    

# Create custom user groups
view_group, _ = Group.objects.get_or_create(name='Viewers')
change_group, _ = Group.objects.get_or_create(name='Changers')
delete_group, _ = Group.objects.get_or_create(name='Deleters')

