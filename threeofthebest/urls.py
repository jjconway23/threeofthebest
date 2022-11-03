from django.contrib import admin
from django.urls import path, include
from django.conf import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400="theblog.views.handle_bad_error"
handler401="theblog.views.handle_unauthorized_access"
handler404="theblog.views.handle_not_found"
handler500="theblog.views.handle_unexpected_condition"
handler503="theblog.views.handle_server_unavailable"
handler504="theblog.views.handle_temporary_error"
