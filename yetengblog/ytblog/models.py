from django.db import models

class YtArticle(models.Model):
    title=models.CharField(max_length=32,null=False)
    content=models.TextField(null=True)
    pubtime=models.DateTimeField(null=True)

    def __str__(self):
        return self.title
