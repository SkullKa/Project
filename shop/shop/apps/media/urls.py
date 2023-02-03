from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # path('upload/', views.image_upload_view),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)