from email.mime import image
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import addMember
from django.contrib.auth.models import User,auth
       
# Create your views here.




def login(request):
    if request.method == 'POST' :
        username=request.POST['Username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/dashboard/')
        else:
            messages.info(request,"invalid credentails")
          
        
    else:
        return render(request,'signin.html')
   
def signup(request):
    if request.method == 'POST' :
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['Username']
        password=request.POST['password']
        
        date=request.POST['date']
        gender=request.POST['gender']
        age=request.POST['age']

        if len(request.FILES) !=0:
            image=request.FILES['photo']
        member=addMember(fname=fname,lname=lname,username=username,age=age,gender=gender,password=password,date=date,image=image)
        user=User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
        user.save()
        member.save()
        return HttpResponseRedirect('/accounts/login/')
        # messages.success(request,"Add member successfully")
    

    return render(request,'signup.html')