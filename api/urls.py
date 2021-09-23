from django.urls import path, include
from api import views
from rest_framework import routers

# Adding urls for routers
router = routers.DefaultRouter()
router.register('developer-profile', views.DeveloperProfileViewSet)
router.register('generate-music', views.MusicReportViewSet)
#router.register('image-report', views.ImageReportViewSet)
#router.register('video-report', views.VideoReportViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path('developer-accessToken/', views.DeveloperLoginApiView.as_view()),
]