from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.CourseDetail)
admin.site.register(models.Chapter)