from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from filmo.views import (
    DirectorViewSet,
    ActorViewSet,
    MovieViewSet,
    ScriptViewSet,
    PlayViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()
router.register('director', DirectorViewSet, basename='Directors')
router.register('actor', ActorViewSet, basename='Actors')
router.register('movie', MovieViewSet, basename='Movies')
router.register('script', ScriptViewSet, basename='Scripts')
router.register('play', PlayViewSet, basename='PlayedIn')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path("api/", include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
