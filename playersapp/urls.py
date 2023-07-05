from rest_framework import routers

from .views import PlayerViewSet

router = routers.DefaultRouter()
router.register('players', PlayerViewSet)
