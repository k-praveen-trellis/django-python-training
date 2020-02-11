from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product

def product_home(request):
    products = Product.objects
    return render(request,'products/products.html',{'products':products})

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
        return redirect('/products/'+str(product.id))
    else:
        return render(request,'products/create.html')


def detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/details.html',{'product':product})

@login_required
def upvote(request,product_id):
    if request.method=="POST":
        product = get_object_or_404(Product,pk=product_id)
        product.votes_count+=1
        product.save()
        return redirect('/products/'+str(product_id))

def search(request):
    product = Product.objects
    if request.method == 'GET':
        search_text =  request.GET['search']
        status = product.filter(body__icontains=search_text)
        if status:
            return render(request,"products/products.html",{"search_result":status})
        else:
            return render(request,"products/products.html",{'error':'not found'})
