from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("resolved", "Resolved"),
            ("closed", "Closed"),
        ],
        default="new",
    )

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Us"


class ReportIssue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    reported_by = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("open", "Open"),
            ("in_progress", "In Progress"),
            ("resolved", "Resolved"),
            ("closed", "Closed"),
        ],
        default="open",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Report Issue"
        ordering = ["-created_at"]


class ReportComment(models.Model):
    comment = models.ForeignKey(
        "blog.comment", on_delete=models.CASCADE, related_name="reported_comment"
    )
    reason = models.TextField()
    reported_by = models.ForeignKey(
        "user.user",
        on_delete=models.CASCADE,
        related_name="reporter",
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("open", "Open"),
            ("in_progress", "In Progress"),
            ("resolved", "Resolved"),
            ("closed", "Closed"),
        ],
        default="open",
    )
