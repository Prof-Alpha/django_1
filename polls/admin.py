from django.contrib import admin
from polls.models import Questions, Choices

# Register your models here.

admin.site.register(Questions)
admin.site.register(Choices)