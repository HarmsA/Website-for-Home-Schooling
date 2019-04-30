from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    context = {
        'title': "Login"
    }
    return render(request, 'login/login.html', context)

def process_login(request):
    return redirect('/login/login')

def register(request):
    return redirect('/login/login')

def process_register(request):
    return redirect('/login/login')