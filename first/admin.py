from django.contrib import admin

import first.models

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'janre')
    list_display_links = ('id', 'author')
    ordering = ('-author',)
    search_fields = ('id', 'author', 'name')




admin.site.register(first.models.Janre)
admin.site.register(first.models.Author)
admin.site.register(first.models.Book, BookAdmin)
admin.site.register(first.models.USD)