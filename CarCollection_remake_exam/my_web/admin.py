from django.contrib import admin

from CarCollection_remake_exam.my_web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'age',)
