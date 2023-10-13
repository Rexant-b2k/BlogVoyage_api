from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
