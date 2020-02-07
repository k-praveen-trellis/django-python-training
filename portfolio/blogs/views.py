from django.shortcuts import render
from .models import Blog
import random
# Create your views here.
def blog_home(request):
    blogs_  = Blog.objects
    # colors = ['green','red','orange','yellow','pink','blue']
    # ,'colors':colors[random.randint(0,5)]
    return render(request,'blogs/blogs.html',{'blogs':blogs_})
