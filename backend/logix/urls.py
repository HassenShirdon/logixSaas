from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hrm.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/', include('operations.urls')),
    path('api/', include('finance.urls')),
]
