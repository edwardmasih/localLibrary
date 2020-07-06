from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect('login')
 
    else:
        f = RegisterForm()
 
    return render(request, 'register/register.html', {'form': f})