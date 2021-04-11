"""
Definition of models.
"""

from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib import admin        # Add administrative module use
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Model of the data Blog
class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date='posted', verbose_name='Article')
    description = models.TextField(verbose_name='Synopsis') # Synopsis = short description
    content = models.TextField(verbose_name='Full description')
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Publicated')
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Author")


    def get_absolute_url(self):         # method returns string with unique Internet-address post
        return reverse('blogpost', args=[str(self.id)])

    def __str__(self):                  # method returns name of the different posts
        return self.title

    class Meta:
        db_table = 'Posts'                  # name of the DB table
        ordering = ['-posted']              # order of sort data in model ("-" - descending)
        verbose_name = 'blog post'          # name that can we see in administration module
        verbose_name_plural = 'blog post'   # for all posts in blog


admin.site.register(Blog)


class Comment(models.Model):
    text = models.TextField(verbose_name = "Comment")
    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Post')

    def __str__(self):
        return 'Comment %s for %s' % (self.author, self.post)

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments for blog posts'
        ordering = ['-date']

admin.site.register(Comment)