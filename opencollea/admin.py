from django.contrib import admin
from opencollea.models import *


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'first_name', 'last_name',
              'email', 'avatar', 'website']
    list_display = ('username', 'first_name', 'last_name', 'email')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'machine_readable_title')


class ReferenceTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'machine_readable_title')


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'user')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('content', 'question', 'user')

# Register models to admin area
admin.site.register(Course)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Attachment)
admin.site.register(ReferenceType, ReferenceTypeAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
