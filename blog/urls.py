from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog', views.BlogView)

urlpatterns = [
path('', include(router.urls))    
   
]