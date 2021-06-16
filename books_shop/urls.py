import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("sales_manager.urls")),
    path('accounts', include("sales_manager.urls")),
    path('hotel/', include("hotel.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
