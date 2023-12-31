from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from schema_graph.views import Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('profiles.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
