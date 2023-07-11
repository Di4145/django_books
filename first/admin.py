from django.contrib import admin

import first.models

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name')
    list_display_links = ('id', 'author')
    ordering = ('-author',)
    search_fields = ('id', 'author', 'name')




admin.site.register(first.models.Book, BookAdmin)