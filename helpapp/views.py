from django.shortcuts import render
from .forms import UploadForm
from .models import Upload
# Create your views here.
def upload(request):
    form_class=UploadForm
    if request.method=="POST":
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=UploadForm
    images=Upload.objects.all()
    return render(request,'home.html',{'images':images,'form':form})