from django.contrib import admin
from django.urls import path
from django.urls import include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Base API Endpoints
    path('api/v1/', include('api.urls')),
]
