from django.db import models

# Create your models here.
class createTicket(models.Model):
    user_id = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    CATEGORY_CHOICES = [
    ('technical', 'Technical'),
    ('billing', 'Billing'),
    ('general', 'General'),
    ('others', 'Others'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    uploaded_file = models.FileField(upload_to='upload/')

    create_at = models.DateTimeField(auto_now_add=True)

