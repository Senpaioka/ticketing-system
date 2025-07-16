from django.db import models
from account.models import UserAccount

# Create your models here.
class createTicket(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
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

    uploaded_file = models.FileField(upload_to='upload/', null=True, blank=True)

    TICKET_STATUS = [
        ('open', 'Open'),
        ('progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    status = models.CharField(max_length=20, choices=TICKET_STATUS, default='open')

    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

