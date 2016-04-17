import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Post(models.Model):

    def __str__(self):
	    return self.post_title
    def __str__(self):
    	return self.post_content
    def __str__(self):
    	return self.username
    def __str__(self):
    	return self.password
    def blog_id(self):
    	return self.blog_id
    def post_author(self):
    	return self.post_author

    def datetime(self):
    	return now
    now=timezone.now()
    def __str__(self):
    	return self.post_format


    post_status = "publish"
    comment_status = "open"
    post_parent = 0
    post_format = "standard"
    post_excerpt = ""
    post_type = "post"
    ping_status = "open"
    sticky = 0


    post_title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    body = models.CharField(max_length=10000)

class Comment(models.Model):
    def __str__(self):
        return self.comment_text
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
