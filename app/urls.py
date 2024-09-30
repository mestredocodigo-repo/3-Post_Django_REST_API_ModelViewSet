from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category',CategoryView)
router.register(r'company',CompanyView)
router.register(r'medicine',MedicineView)

urlpatterns = router.urls
