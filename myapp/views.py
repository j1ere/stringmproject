from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('stringm')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'index.html', {'form':form})

#usercreation
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stringm')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})

def stringm(request):
    return render(request, 'stringm.html')