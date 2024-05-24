from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

STATUS = (0, 'Draft'), (1, 'Published')


class Post(models.Model):
    """
    Model representing a post.
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True,)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        String representation of the Post model.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Save the Post instance.
        Automatically generate slug if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def number_of_likes(self):
        """
        Return number of likes for the post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model representing a comment on post.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """
        String representation of the Comment model.
        """
        return f'Comment {self.body} by {self.name}'


class TeamMember(models.Model):
    """
    Model representing a team member.
    """

    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        """
        String representation of the TeamMember model.
        """
        return self.name
