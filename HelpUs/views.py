from django.shortcuts import render,redirect
from django.http import HttpResponse
from helpapp.models import *
from django.shortcuts import render
from helpapp.forms import UploadForm
from helpapp.models import Upload
def show_about_page(request): 
    print("hello there!")
    name="freeCodeHub"
    link="https://www.youtube.com/freecodehub"

    data={
        'name':name,
        'link':link

    }
    return render(request,"about.html",data)

def show_home_page(request):
    if request.method=="POST":
       
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=UploadForm()
    img=Upload.objects.all()

    loc=Location.objects.all()
    images=Image.objects.all()

    data={
        'images':images,
        'loc':loc
    }
    return render(request,'home.html',{
        'images':images,
        'loc':loc,
        'form':form
    })

def show_Location_page(request,cid):
    loc=Location.objects.all()
    locs =Location.objects.get(pk=cid)
    if request.method=="POST":
       
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=UploadForm()
    image=Upload.objects.all()




    images=Image.objects.filter(loc=locs)
    data={
        'images':images,
        'loc':loc,
        'form':form
    }
    return render(request,'home.html',data)
def home(request):
    return redirect('/home')

def upload(request):
    print("UPLOADED")
    if request.method=="POST":
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=UploadForm()
    img=Upload.objects.all()
    return render(request,'home.html',{'img':img,'form':form})