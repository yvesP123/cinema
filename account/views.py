from django.shortcuts import render
from dashboard.models import addMovie
# Create your views here.
def homepage(request):
    movie=addMovie.objects.all()
    return render(request,'index.html',{'movie':movie})
