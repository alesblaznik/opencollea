from django.contrib import admin
from find_courses.models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'url')

# Register models to admin area
admin.site.register(Course, CourseAdmin)
