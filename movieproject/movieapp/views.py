from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import movie
from. forms import movie_form


def index(request):
    # return HttpResponse("hello world")
    movi=movie.objects.all()
    context={
        'movi_list':movi
    }
    return render(request,"index.html",context)
def detail(request,movi_id):
    moviee=movie.objects.get(id=movi_id)
    # return HttpResponse("this is movie no %s"% movi_id)
    return render(request,"detail.html",{'movies':moviee})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movi=movie(name=name,desc=desc,year=year,img=img)
        movi.save()

    return render(request,"add.html")
def update(request,id):
    movi=movie.objects.get(id=id)
    form=movie_form(request.POST or None, request.FILES, instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movi':movi})

def delete(request,id):
    mov = movie.objects.get(id=id)
    if request.method=='POST':
        mov.delete()
        return redirect('/')
    return render(request,"delete.html")