from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    gov_registry = models.CharField(max_length=13)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Companies'
    def __str__(self):
        return self.name
    
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    category_fk = models.ForeignKey(Category, related_name="medicineCategory", on_delete=models.CASCADE)
    company_fk = models.ForeignKey(Company, related_name="medicineCompany", on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    is_generic = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
