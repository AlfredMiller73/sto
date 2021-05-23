from django.urls import path  
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
  
app_name = 'blog'  
  
urlpatterns = [  
    path('', views.blog, name='blog'),
    path('<id>/', views.blogpost, name='blogpost'),
    path('newpost', views.newpost, name='newpost'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
