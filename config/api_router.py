from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path

from onepageapi.stats.views import TgUserView, UserForcingView
from onepageapi.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path('tgUser/', TgUserView.as_view(), name='tg-user'),
    path('statUser/', UserForcingView.as_view(), name='stat-user'),
]
