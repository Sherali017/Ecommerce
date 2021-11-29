from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class AuthorModel(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='authors')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostTagModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post')
    banner = models.ImageField(upload_to='post_banner')
    content = RichTextUploadingField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(PostTagModel, related_name='posts')

    created_at = models.DateTimeField(auto_now_add=True)


    def get_comment(self):
        return self.comments.order_by('-created_at')

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=15, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'



