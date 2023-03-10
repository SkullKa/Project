from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('category/', views.product, name='product'),
    path('category/<int:category_id>/item<int:product_id>/', views.detail, name='detail'),
    path('category/<int:category_id>/', views.catalog, name='catalog'),
    path('upload/', views.image_upload_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)