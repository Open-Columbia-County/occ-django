from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('uc/', views.uc),
    path('projects/', views.projects),
    path('codeOfConduct/', views.codeOfConduct),
    path('members/', views.members),
    path('join/', views.join),
    path('project/<int:project_id>/view', views.viewProject),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)