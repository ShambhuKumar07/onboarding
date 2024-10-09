from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import CustomAuthenticationForm
# Create your views here.

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request=request,data=request.POST)
#         if form.is_valid():
#             login(request, form.user_cache)
#             return redirect("core:main_page")
#     else:
#         form = CustomAuthenticationForm()
#     return render(request,'users/login.html',{'form':form})

########################################


from django.contrib.auth import login
from django.shortcuts import redirect

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             login(request, form.user_cache)
#             if hasattr(request.user, 'applicant'):
#                 return redirect('applicant:dashboard')  # Redirect to applicant dashboard
#             else:
#                 return redirect('core:main_page')
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})




###################################


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            try:
                if request.user.applicant:  # Trying to access the related applicant
                    return redirect('applicant:dashboard')
            except request.user._meta.model.applicant.RelatedObjectDoesNotExist:
                return redirect('core:main_page')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})



def logout_view(request):
    logout(request)

    return redirect('users:login_view')