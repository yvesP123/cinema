from dataclasses import field
from email.mime import image
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from accounts.models import addMember
from dashboard.models import addMovie
from django.views.decorators.cache import cache_control

    
# Create your views here.
def dashboards(request):
    movie=addMovie.objects.filter(status=1)
   
    

   
    return render(request,'user.html',{'movie':movie})
def restore(request,id):
    movie=addMovie.objects.get(id=id)
    movie.status=1
    movie.save()
    return redirect('/dashboard/trash')
def search(request):
    if request.method =='POST':
        titles=request.POST['search']
    querys=addMovie.objects.filter(title=titles)

    return render(request,'search.html',{'querys':querys})
@cache_control(no_cache=True,must_revalidate=True,no_store=True)   
def logout(request):
    return redirect('/accounts/login/')
def delete(request,id):
    m=addMovie.objects.get(id=id)
    m.delete()
    return redirect('/dashboard/trash')
def edit(request,id):
    movies=addMovie.objects.get(id=id)
    return render(request,'edit.html',{'movies':movies})
def update(request,id):
    if request.method =='POST':
        title=request.POST['title']
        actor=request.POST['actors']
        poster=request.POST['poster']
        traier=request.POST['trailer']
        category=request.POST['category']
        user_poster=request.POST['users']
    movies=addMovie.objects.get(id=id)
    movies.title=title
    movies.actor=actor
    movies.poster=poster
    movies.trailer=traier 
    movies.category=category
    movies.user_post=user_poster
    movies.save()   
    return redirect('/dashboard/')
def Hide(request,id):
    m=addMovie.objects.get(id=id)
    # m=addMovie(id=id)
    m.status=0
    m.save()
    return redirect('/dashboard/') 
def trash(request):
    trash=addMovie.objects.filter(status=0)
    return render(request,'hide.html',{'trash':trash})
def favorite(request,get_username):
    favorite=addMovie.objects.filter(user_post=get_username)
    return render(request,'tables-general.html',{'favorite':favorite})   
def add(request):
    if request.method =='POST':
        title=request.POST['title']
        actor=request.POST['actors']
        poster=request.POST['poster']
        traier=request.POST['trailer']
        description=request.POST['description']
        category=request.POST['category']
        date=request.POST['date']
        user_poster=request.POST['users']
        if len(request.FILES) !=0:
            images=request.FILES['image']
        movie=addMovie(title=title,actor=actor,poster=poster,trailer=traier,image=images,realedate=date,description=description,category=category,user_post=user_poster,status=1)
        movie.save()
        return HttpResponseRedirect('/dashboard/')
       

    return render(request,'forms-elements.html')
def profile(request):
    return render(request,'users-profile.html')

     
   
   
