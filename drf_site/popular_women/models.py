from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Woman(models.Model):
    title = models.CharField(max_length=200, editable=True, null=True)
    content = models.TextField(blank=True, editable=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_updated = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True, null=True)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


