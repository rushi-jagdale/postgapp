from django.shortcuts import render,redirect

from ticaret.models import Destination
from django.contrib import messages 
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):

    return render(request,'home.html')

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)   
            return redirect('/')

        else:
            messages.info(request, 'invalid username and password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {"dests":dests})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken..')
               
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken ..')
                
                return redirect('register')

            else: 
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User Created Successfully ..')
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'Password is not matching ..')
            print('password not matching')
            return redirect('register')


        return redirect('/')

    else:
        
        return render(request,"register.html")    

def logout(request):
    auth.logout(request)
    return redirect('/')        