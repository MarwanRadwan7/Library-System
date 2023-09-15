from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.conf.urls import handler404
from books.views import lms_index

urlpatterns = [
    path('' , lms_index , name='LMS_index'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('students/', include('students.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'students.views.error_404'