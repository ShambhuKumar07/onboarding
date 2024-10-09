from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import Employee

def add_employee(request):
    if request.method == 'POST':
        uan_number = request.POST.get('uan_number')
        pan_number = request.POST.get('pan_number')
        esic_number = request.POST.get('esic_number')

        # Create and save a new employee record
        Employee.objects.create(uan_number=uan_number, pan_number=pan_number, esic_number=esic_number)
        
        # Redirect to a success page or any other view
        return redirect('employee_success')
    
    return render(request, 'compliance/employee_form.html')


def employee_success(request):
    return render(request, 'compliance/employee_success.html')
