from django.contrib import admin
from .models import Callback, Feedback, Comment, About

admin.site.register(Callback)
admin.site.register(Feedback)
admin.site.register(Comment)
admin.site.register(About)