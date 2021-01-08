"""RestAPIView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import classviews, functionviews, modelviewsetviews, genericviews, viewsetviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empmv', modelviewsetviews.employeeViewSet)
router.register(r'empv', viewsetviews.employeeViewSet, basename='empv')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('empcv/', classviews.employeeList.as_view(), name="emp_list"),
    path('empcv/<int:pk>/', classviews.employeeList.as_view(), name="emp_detail"),
    path('emp/', functionviews.employeeList, name="emp_list"),
    path('emp/<int:pk>/', functionviews.employeeList, name="emp_detail"),
    path('empgv/', genericviews.employeeList.as_view(), name="emp_list"),
    path('empgv/<int:pk>/', genericviews.employeeDetail.as_view(), name="emp_detail"),
    path('xml/', functionviews.xmlview),
]

urlpatterns += router.urls
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'xml', 'html', 'yaml'])