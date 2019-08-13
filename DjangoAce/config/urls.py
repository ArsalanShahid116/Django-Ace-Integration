from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import coder.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coder/', include('coder.urls')),
]
