from django.contrib import admin
from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    # View the post fields dispayable for the admin
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    # Add a field for post text search
    search_fields = ('text',)
    # Add a field to filter by pub date
    list_filter = ('pub_date',)
    # Add a filler for blank values
    empty_value_display = '-empty-'


class GroupAdmin(admin.ModelAdmin):
    # View the group fields dispayable for the admin
    list_display = ('pk', 'title', 'slug', 'description',)
    # Add a field for group search
    search_fields = ('title', 'description',)
    # Add a field to filter by pub date
    # list_filter = ('pub_date',)
    # Add a filler for blank values
    # empty_value_display = '-empty-'


# Once registered, each model is ruled by its view manager class
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
