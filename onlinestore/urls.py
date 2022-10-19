
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings

from feedbacks.urls import urlpatterns as feedbacks_urls
from items.urls import urlpatterns as items_urls
from users.urls import urlpatterns as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(items_urls)),
    path('', include(feedbacks_urls)),
    path('', include(users_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
