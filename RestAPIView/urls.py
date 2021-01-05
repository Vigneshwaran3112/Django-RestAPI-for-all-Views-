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
from app1 import classviews, functionviews, modelviewsetviews, genericviews, viewsetviews
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('emp', modelviewsetviews.employeeViewSet)
router.register(r'emp', viewsetviews.employeeViewSet, basename='emp')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('emp/', classviews.employeeList.as_view(), name="emp_list"),
    # path('emp/<int:pk>/', classviews.employeeList.as_view(), name="emp_detail"),
    # path('emp/', functionviews.employeeList, name="emp_list"),
    # path('emp/<int:pk>/', functionviews.employeeList, name="emp_detail"),
    # path('emp/', genericviews.employeeList.as_view(), name="emp_list"),
    # path('emp/<int:pk>/', genericviews.employeeDetail.as_view(), name="emp_detail"),
    path('', include(router.urls)),
]
