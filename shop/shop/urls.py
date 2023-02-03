from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('', include('users.urls')),
    path('upload/', include('media.urls')),
    # path('upload/', views.image_upload_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)