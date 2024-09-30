from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MedicineView(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

