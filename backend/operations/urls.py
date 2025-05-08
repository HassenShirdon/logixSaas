from django.urls import path, include
from .views import operations
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'employees', EmployeeViewSet) # commented out for now
# router.register(r'departments', DepartmentViewSet) # commented out for now
urlpatterns = [
    path('operations/', operations, name="operations"),
    path('', include(router.urls)),
]