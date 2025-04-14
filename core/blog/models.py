from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    body = models.TextField(null=False)
    author = models.ForeignKey(
        "user.user", related_name="blogs", null=False, on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(upload_to="blog/thumbnails/", null=True, blank=True)
    # tags = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    blog = models.ForeignKey(
        "blog.Blog", related_name="comments", null=False, on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        "user.user", related_name="comments", null=False, on_delete=models.CASCADE
    )
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    author = models.ForeignKey(
        "user.user", related_name="likes", null=False, on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        "blog.Blog", related_name="likes", null=False, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("author", "blog")
