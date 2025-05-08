from django.urls import path,include
from .views import finance
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'employees', EmployeeViewSet) # commented out for now
# router.register(r'departments', DepartmentViewSet) # commented out for now
urlpatterns = [
    path('finance/', finance, name="finance"),
    path('', include(router.urls)),
]