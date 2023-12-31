from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('news/',  include('news.urls')),
    path('games/', include('games.urls')),
    path('soft/', include('soft.urls')),
    path('cookie/', include('cookie.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

