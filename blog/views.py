from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from newBlog.models import Write
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    blogs = Write.objects.all()

    context = {
        "blogs":blogs
    }
    return render(request,'home.html',context)

def blog_by_id(request,id):
    blog = get_object_or_404(Write,id=id)
    context = {
        "blog":blog
    }
    return render(request,'blog.html',context)

def create_blog(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        user = request.user

        new_post = Write.objects.create(title=title,description=desc,user=user)
        new_post.save()

        return redirect("home")
    else:
        HttpResponse("Error creating post")
    
    return render(request,'createBlog.html')

    