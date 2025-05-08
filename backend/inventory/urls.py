from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, PurchaseOrderViewSet, GoodsReceiptViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'goods-receipts', GoodsReceiptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
