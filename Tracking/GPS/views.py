from .decorators import unauthenticated_user,allowed_users,admin_only
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .filters import LocationFilter



@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username =form.cleaned_data.get('username')
            group = Group.objects.get(name='users')
            user.groups.add(group)
            messages.success(request,'Account was created for '+username)
            return redirect('login')

    context={'form':form}
    return render(request,'register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request,'Username or password is not correct')


    context={}
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    users=User.objects.filter(groups__name='users')
    context={'users':users}
    return render(request,'users.html',context)


@login_required(login_url='login')   
def userPage(request):
    devices=request.user.device_set.all()
    context={'devices':devices}
    return render(request,'dashboard.html',context)



@login_required(login_url='login')   
@admin_only 
def user_from_admin(request,pk):
    user=User.objects.get(id=pk)
    devices=user.device_set.all()
    context={'devices':devices}
    return render(request,'dashboard.html',context)



@login_required(login_url='login')
@admin_only 
def delete_user(request, pk):
	user = User.objects.get(id=pk)
	if request.method == "POST":
		User.delete(user)
		return redirect('home')

	context = {'item':user}
	return render(request, 'delete_user.html', context)



@login_required(login_url='login')
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            category=form.cleaned_data["category"]
            description=form.cleaned_data["description"]
            request.user.device_set.create(name=name,category=category,description=description)
            return redirect('home')

    else: 
        form = DeviceForm()
    return render(request, 'add_device.html', {'form':form}) 
	       

@login_required(login_url='login')
def update_device(request, pk):

	device = Device.objects.get(id=pk)
	form = DeviceForm(instance=device)

	if request.method == 'POST':
		form = DeviceForm(request.POST, instance=device)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'update_device.html', context)
			

@login_required(login_url='login')
def delete_device(request, pk):
	device = Device.objects.get(id=pk)
	if request.method == "POST":
		Device.delete(device)
		return redirect('home')

	context = {'item':device}
	return render(request, 'delete_device.html', context)



@login_required(login_url='login')
def device(request,pk):
    device = Device.objects.get(id=pk)
    locations=device.location_set.all()
    myFilter = LocationFilter()
    myFilter = LocationFilter(request.GET, queryset=locations)
    locations = myFilter.qs 
    context={'locations':locations,'device':device,'myFilter':myFilter}
    return render(request, 'device.html',context)




@login_required(login_url='login')
def track(request,pk):
    device = Device.objects.get(id=pk)
    
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            longitude=form.cleaned_data["longitude"]
            latitude=form.cleaned_data["latitude"]
            device.location_set.create(longitude=longitude,latitude=latitude)
            return redirect('device',pk=device.id)

    else: 
        form = LocationForm()
    return render(request, 'add_location.html', {'form':form}) 


# Create your views here.
