from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth


from . models import   Bank
# from . models import About
# from . models import login
# Create your views here.
def home(request):
    obj=Bank.objects.all()
    return render(request,'index.html',{'result':obj})

def img(request):
    img=Bank.objects.all()
    return render(request,'index.html',{'results':img})

def About(request):
    obj1= About.objects.all()
    return render(request,'index.html',{'result1':obj1})


def login(request):
    if request.method == 'POST':
        # Validate the form data
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username and password are correct
        if username == 'admin' and password == 'password':
            # Redirect to the new page
            return redirect('new_page')
        else:
            # Return an error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # Display the login form
        return render(request, 'login.html')


def Register(request):
  if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Register(request, user)
            return redirect("bank:register.html")
  form = UserCreationForm
  return render(request = request,
                  template_name = "register.html",
                  context={"form":form})


def new_page(request):
    return render(request, 'new_page.html')

def new(request):
    return render(request, 'new.html')