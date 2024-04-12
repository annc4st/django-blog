from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.CharField(max_length=256, default="default")
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:70] + "..."
    