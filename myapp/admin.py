from django.contrib import admin
from myapp.models import Posting

class PostingAdmin(admin.ModelAdmin):
  list_display = ('id', 'message', 'created_at')

admin.site.register(Posting, PostingAdmin)