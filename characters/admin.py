from django.contrib import admin

# Register your models here.

from .models import Question, Character
admin.site.register(Question)
admin.site.register(Character)
