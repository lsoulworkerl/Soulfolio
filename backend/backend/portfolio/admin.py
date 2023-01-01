from django.contrib import admin
from .models import Introduction, AccountLinks, Projects, Timeline


@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(AccountLinks)
class AccountLinksAdmin(admin.ModelAdmin):
    list_display = ('social',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('date',)