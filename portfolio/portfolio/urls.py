from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views as jv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jv.jobs_home,name='jobhome'),
    path('blogs/',include('blogs.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
