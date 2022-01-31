from django.urls import include, path
from rest_framework import routers
from we_can.user.views import UserViewSet, PostPoints, Register, KarmaBoard
from we_can.can.views import CanViewSet, BinReported, RequestBin
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'can', CanViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/<str:name>', Register.as_view()),
    path('user/<str:user_id>/can/<int:can_id>', PostPoints.as_view()),
    path('can/<int:can_id>/user/<str:user_id>/report', BinReported.as_view()),
    path('user/<str:user_id>/can/request', RequestBin.as_view()),
    path('karmaboard', KarmaBoard.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]