from django.db import models
from django.utils.text import slugify
from django.conf import settings
class Article(models.Model):
   title = models.CharField(max_length=200, unique=True)
   image = models.ImageField(upload_to="articles/", null=True, blank=True)
   slug = models.SlugField(max_length=220, unique=True, blank=True)
   content = models.TextField()
   author = models.ForeignKey(
       settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True, blank=True,
       related_name="articles",)#related names for view
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
       return self.title
   def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       super().save(*args, **kwargs)
