from django.contrib import admin
from models import *
# Register your models here.
#
class DocumentAdmin(admin.ModelAdmin):
  list_display = ('docfile',)

admin.site.register(Document, DocumentAdmin)

