from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Administration"
admin.site.site_header = "Blogs Administration"
admin.site.site_title = "RadioWebstar Blogs"
