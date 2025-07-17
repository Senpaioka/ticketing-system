from django.contrib import admin
from ticket.models import createTicket, CommentModel
# Register your models here.

admin.site.register(createTicket)
admin.site.register(CommentModel)
