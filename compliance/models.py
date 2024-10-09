from django.db import models

# Create your models here.

class Employee(models.Model):
    uan_number = models.CharField(max_length=12, unique=True, verbose_name="UAN No.")
    pan_number = models.CharField(max_length=10, unique=True, verbose_name="PAN No.")
    esic_number = models.CharField(max_length=17, unique=True, verbose_name="ESIC No.")

    def __str__(self):
        return f"{self.pan_number} - {self.uan_number}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['pan_number']  # Optional: Orders by PAN No.
