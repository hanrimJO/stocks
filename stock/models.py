from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(max_length=50)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=100)

    def __str__(self):
        return [self.user_id, self.user_email, self.user_name, self.user_phone]


class Company(models.Model):
    company_code = models.IntegerField(max_length=100)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return [self.company_name, self.company_code]


class Stock(models.Model):
    company_name = models.ForeignKey(Company.company_name, on_delete=models.CASCADE)
    company_code = models.ForeignKey(Company.company_code, on_delete=models.CASCADE)
    saved_time = models.DateTimeField(auto_now_add=True)
    saved_day = models.DateField(auto_now_add=True)
    company_stock = models.CharField(max_length=200)

    def __str__(self):
        return [self.company_name, self.company_stock, self.company_stock, self.saved_time, self.saved_day]



