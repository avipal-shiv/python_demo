
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sitepanel/', admin.site.urls),
    path('', include('home_app.urls')),
    path('', include('register_app.urls')),
    path('', include('myaccount_app.urls')),
    path('', include('task_app.urls')),
    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'To Do Adminsitration'  
admin.site.index_title = 'To Do'  # default: "Site administration"
admin.site.site_title = 'To Do' # default: "Django site admin"

handler404 = 'home_app.views.error_404_view'
