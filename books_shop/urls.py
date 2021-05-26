import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("sales_manager.urls")),
    path('accounts', include("sales_manager.urls")),
    path('hotel/', include("hotel.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
]
