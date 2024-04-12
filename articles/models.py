from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #add thumbanail
    #add author
    
    def __str__(self):
        return self.title
    