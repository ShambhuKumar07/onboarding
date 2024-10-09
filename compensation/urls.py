 
from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView

from .views import employee_ctc_view

urlpatterns = [
    path('compensation/employee/ctc/', employee_ctc_view, name='employee_ctc'),
    path('success/', TemplateView.as_view(template_name='compensation/success.html'), name='success_page'),
]
