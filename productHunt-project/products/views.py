from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product

def product_home(request):
    return render(request,'products/products.html')

@login_required
def create_blog(request):
    if request.method=="POST":
        product = Product()
        product.title = request.POST['input_title']
        product.body = request.POST['input_body']
        product.url = request.POST['input_title']
        product.image = request.FILES['input_image']
        product.pub_date = timezone.datetime.now()
        product.votes_count = 1
        product.main_user_hunter = request.user
        product.save()
        return redirect('product_home')
    else:
        return render(request,'products/create.html')
