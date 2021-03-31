from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,ProductForm
from django.contrib.auth import authenticate,login,logout
from .models import Product

def indexview(req):
     request = req
     template_name = "app1/index.html"
     context = {}
     return render(request,template_name,context)


def regview(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = "app1/register.html"
    context = {'form': form}
    return render(request,template_name,context)


def logview(request):
    if request.method == 'GET':
        template_name = "app1/login.html"
        context = {}
        return render(request,template_name,context)
    else:
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u,password=p)
        if user is not None:
            login(request,user)
            return redirect('products')
        else:
            return HttpResponse("Invalid Credentials!")

def loutview(request):
    logout(request)
    return redirect('login')


def addProduct(request):
    if request.method =='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            Product.merchant_user = request.user
            Product.save()
            return redirect('productlist.html')
        else:
            form=ProductForm()
            template_name = "app1/addproduct.html"
            context = {'form' : form}
            return render(request,template_name,context)



def productlistview(request):
    objs = Product.objects.all()
    template_name = 'app1/productlist.html'
    context = {'productlist': objs}
    return render(request, template_name, context)