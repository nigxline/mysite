from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.CharField(max_length=200)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default='菽绣')
    page_view = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title


class BgRecord(models.Model):
    created_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_time']

class BlogRoll(models.Model):
    friend = models.CharField(max_length=30)
    link = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.CharField(max_length=20)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now=True)

class WordsOfQiu(models.Model):
    content = models.TextField()
    date = models.CharField(max_length=25)

    class Meta:
        db_table = 'WordsOfQiu'
        ordering = ['-id']