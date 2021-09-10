from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users import views as users_views
from app_api import views as app_api_views

router = routers.DefaultRouter(trailing_slash=False)

# app_api views
router.register(r'school', app_api_views.SchoolView, 'school')
router.register(r'subjects', app_api_views.SubjectView, 'subjects')
router.register(r'professor', app_api_views.ProfessorView, 'professor')
router.register(r'teacher_rate', app_api_views.ReviewView, 'teacher_rate')

# users views
router.register(r'auth', users_views.AuthViewSet, 'auth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
