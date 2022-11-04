from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foot_space.urls')),
    path('blog_auth/', include('django.contrib.auth.urls')),
    path('blog_auth/', include('blog_auth.urls')),
]
