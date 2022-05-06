
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.content[:20]}"


class Comment(models.Model):
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.post.title} | {self.content[:20]}"
