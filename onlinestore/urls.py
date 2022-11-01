
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings

from feedbacks.urls import urlpatterns as feedbacks_urls
from products.urls import urlpatterns as product_urls
from users.urls import urlpatterns as users_urls
from main.urls import urlpatterns as main_urls
from orders.urls import urlpatterns as orders_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(product_urls)),
    path('', include(feedbacks_urls)),
    path('', include(users_urls)),
    path('', include(main_urls)),
    path('', include(orders_urls)),

]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
