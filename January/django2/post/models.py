from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    def get_default_user():
        user = User.objects.first()
        return user.id if user else None

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)
    likes = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])

def __str__(self):
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
