from rest_framework.routers import DefaultRouter

from numbasums.views import NumbasumViewSet

router = DefaultRouter()
router.register(r"numbasums", NumbasumViewSet, basename="numbasums")
numbasums_urlpatterns = router.urls