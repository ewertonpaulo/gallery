from django.contrib import admin
from photos import views
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from fui import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add_photo, name = 'add_photo'),
    path('list_photos', views.list_photos, name='list_photos'),
    path('delete_event/<int:id>', views.delete_photo, name='delete_photo'),
    path('review/<int:id>', views.review, name = 'review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)