from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class commentOnPost(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    
    list_filter = ['pub_date']
    search_fields = ['post_title']
    list_display = ('post_title','pub_date')
    fieldsets = [
        (None,               {'fields': ['post_title']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [commentOnPost]

admin.site.register(Post, PostAdmin)