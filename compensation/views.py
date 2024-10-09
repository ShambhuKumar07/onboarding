
from django.shortcuts import render, redirect
from .forms import EmployeeSalaryForm, EmployeeContributionForm, EmployeeDeductionForm
from .models import EmployeeCTC,employee_deduction

def employee_ctc_view(request):
    gross_salary = None  # Initialize gross salary variable
    total_contribution = None  # Initialize total contribution variable
    total_deduction = None  # Initialize total deduction variable
    ctc_value = None  # Initialize CTC variable

    if request.method == 'POST':
        salary_form = EmployeeSalaryForm(request.POST)
        contribution_form = EmployeeContributionForm(request.POST)
        deduction_form = EmployeeDeductionForm(request.POST)

        if salary_form.is_valid() and contribution_form.is_valid() and deduction_form.is_valid():
            # Save all the form data
            salary = salary_form.save()
            contribution = contribution_form.save()
            deduction = deduction_form.save()  # Save the deduction form data

            # Calculate gross salary
            gross_salary = salary.gross_salary()

            # Create an EmployeeCTC object
            ctc = EmployeeCTC.objects.create(salary=salary, contribution=contribution)

            # Calculate CTC (Gross Salary + Employer's Contribution)
            ctc_value = ctc.calculate_ctc()

            # Redirect to a success page or render the same page with success message
            return redirect('success_page')

    else:
        salary_form = EmployeeSalaryForm()
        contribution_form = EmployeeContributionForm()
        deduction_form = EmployeeDeductionForm()

    return render(request, 'compensation/employee_ctc.html', {
        'salary_form': salary_form,
        'contribution_form': contribution_form,
        'deduction_form': deduction_form,
        'gross_salary': gross_salary,  # Pass gross salary to the template
        'total_contribution': total_contribution,  # Pass total contribution to the template
        'total_deduction': total_deduction,  # Pass total deduction to the template
        'ctc_value': ctc_value,  # Pass CTC to the template
    })
