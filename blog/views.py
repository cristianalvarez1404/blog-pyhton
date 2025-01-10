from django.shortcuts import render
from newBlog.models import Write

# Create your views here.
def home(request):
    blogs = Write.objects.all()

    context = {
        "blogs":blogs
    }
    return render(request,'home.html',context)