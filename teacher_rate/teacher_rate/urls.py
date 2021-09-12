from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users import views as users_views
from app_api import views as app_api_views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter(trailing_slash=False)

# app_api views
router.register(r'school', app_api_views.SchoolView, basename='school')
router.register(r'subjects', app_api_views.SubjectView, basename='subjects')
router.register(r'professor', app_api_views.ProfessorView, basename='professor')
router.register(r'teacher_rate', app_api_views.ReviewView, basename='teacher_rate')

# users views
router.register(r'auth', users_views.AuthViewSet, basename='auth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
