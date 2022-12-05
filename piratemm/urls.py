from django.contrib import admin
from django.urls import path, include
from anime import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('anime.urls',namespace='anime')),
    path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
