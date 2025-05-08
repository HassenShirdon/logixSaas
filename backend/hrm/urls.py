from django.urls import path, include
from .views import hrm
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'employees', EmployeeViewSet) # commented out for now
# router.register(r'departments', DepartmentViewSet) # commented out for now
urlpatterns = [
    path('hrm/', hrm, name="hrm"),
    path('', include(router.urls)),
]
