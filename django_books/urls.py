from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from first.views import list_info, book_detail_view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', list_info, name='main_page'),
    path('book/<int:pk>', book_detail_view, name='detail_page')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)