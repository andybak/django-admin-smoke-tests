# Django imports
from django.contrib import admin

# App imports
from .models import Channel, HasPrimarySlug, HasPrimaryUUID, Post


class ChannelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Channel, ChannelAdmin)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ['status']
    list_display = ('title', 'author', 'status', 'modified', 'published',)
    list_filter = ('author', 'status', 'channel', 'created', 'modified',
        'published',)
    readonly_fields = ['created', 'modified', 'time_diff']
    ordering = ('title', '-id',)

    search_fields = ['title', 'text']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            db_field.default = request.user
        return super(PostAdmin, self).formfield_for_foreignkey(db_field,
            request, **kwargs)

admin.site.register(Post, PostAdmin)


admin.site.register(HasPrimarySlug)


if HasPrimaryUUID:
    admin.site.register(HasPrimaryUUID)
