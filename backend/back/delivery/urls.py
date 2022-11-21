from django.urls import path, include
#from . import views
from rest_framework.routers import DefaultRouter
from .views import PostViewset


router = DefaultRouter()
router.register('order', PostViewset)

post_detail = PostViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', include(router.urls)),
    path('detail',post_detail)
    # path('/get',views.get_api),
    # path('/post',views.post_api)
]