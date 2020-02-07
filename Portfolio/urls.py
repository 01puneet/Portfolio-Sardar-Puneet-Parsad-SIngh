
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Carrer.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Carrer.views.home, name='home'),
    path('blog/', include('Blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
