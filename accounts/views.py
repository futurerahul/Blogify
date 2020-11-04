from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def home_page(request):
    return render(request,"accounts/home.html", {'user': request.user})

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,"accounts/register.html",{'form':form})



