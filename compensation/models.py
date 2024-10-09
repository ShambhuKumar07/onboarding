from django.db import models

# Create your models here.
class EmployeeSalary(models.Model):
    basic = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Basic Salary")
    hra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRA")
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Special Allowance")

    def gross_salary(self):
        return self.basic + self.hra + self.special_allowance

    def __str__(self):
        return f"Basic: {self.basic}, HRA: {self.hra}, Special Allowance: {self.special_allowance}"
    
class employee_deduction(models.Model):

    pf_deduction=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="PF_Deduction")
    asic_deduction=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="ASIC_Deduction")
    def emp_deduction(self):
        return self.pf_deduction + self.asic_deduction

    def __str__(self):
        return f"PF_Deduction:{self.pf_deduction}, ASIC_Deduction:{self.asic_deduction}"

class EmployeeContribution(models.Model):
    pf_emp_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="PF (Employers Contribution)")
    esic_emp_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ESIC (Employers Contribution)")
    mediclaim = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Mediclaim")
    gratuity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gratuity")

    # Calculate total employee contribution
    def emp_contribution(self):
        return self.pf_emp_contribution + self.esic_emp_contribution + self.mediclaim + self.gratuity

    def __str__(self): 
        return f"Gratuity: {self.gratuity}, Total Contribution: {self.emp_contribution()}"

# Model to aggregate CTC
class EmployeeCTC(models.Model):
    salary = models.OneToOneField(EmployeeSalary, on_delete=models.CASCADE, verbose_name="Employee Salary")
    contribution = models.OneToOneField(EmployeeContribution, on_delete=models.CASCADE, verbose_name="Employer's Contribution")

    # Calculate CTC (Gross Salary + Employer's Contribution)
    def calculate_ctc(self):
        return self.salary.gross_salary() + self.contribution.emp_contribution()

    def __str__(self):
        return f"CTC: {self.calculate_ctc()}"