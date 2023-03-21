from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

class Status(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.title

class Order(models.Model):
    table = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.table} {self.status}'
