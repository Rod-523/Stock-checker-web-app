from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('stocks/', include('stocks.urls')),
    path('', include('stocks.urls')),
    path('admin/', admin.site.urls),
]
