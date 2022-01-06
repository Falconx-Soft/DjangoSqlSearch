from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CutomUserCreationForm
from SearchApp.models import Reviews

# Create your views here.
@login_required(login_url='login')
def home(request):
	reviews = Reviews.objects.all()
	context = {
		'reviews':reviews
	}
	return render(request,'SearchApp/home.html',context)

def loginUser(request):
	page = 'login'

	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		try:
			user = User.objects.get(username=username)
		except:
			print('User not recognized.')

		user = authenticate(request, username=username, password=password) # check password
		login(request, user)
		return redirect('home')
		
	return render(request,'User/login.html')


def signup(request):

	if request.method == 'POST':
		form = CutomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			return redirect('login')
		else:
			return redirect('signup')
	return render(request,'User/signup.html')

def logoutUser(request):
    logout(request)
    print('User is Loged Out!')
    return redirect('login')