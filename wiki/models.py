from django.db import models
from users.models import User
import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')

class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,null= True, upload_to='images/articles')
    Context = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['html','md','txt'])
    ])
    