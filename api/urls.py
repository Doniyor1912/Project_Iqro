
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView
from api.spectacular.urls import urlpatterns as doc_urls
from project.urls import urlpatterns as showcase
from contact.urls import urlpatterns as contact_urls
from homepage.urls import url_patterns as home_page
from about.urls import urlpatterns as about_us
from project.views import CUpdateimage


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'upload-image', CUpdateimage, basename='uploadimage')


urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += doc_urls
urlpatterns += showcase
urlpatterns += contact_urls
urlpatterns += home_page
urlpatterns += about_us