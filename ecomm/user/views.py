from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,DeleteView
from account.models import products,Cart,Review,Orders
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please Login first!!")
            return redirect("login")
    return inner

dec=[signin_required,never_cache]

# Create your views here.

# class UserHomeView(View):
#     def get(self,request):
#         return render(request,"uhome.html")

@method_decorator(dec,name="dispatch")   
class UserHomeView(TemplateView):
    template_name="uhome.html"

# class ProductsView(TemplateView):
#     template_name="products.html"
    
@method_decorator(dec,name="dispatch")   
class ProductsView(ListView):
    template_name="products.html"
    queryset=products.objects.all()
    context_object_name="products"

    def get_context_data(self, **kwargs):
        res=products.objects.filter(categories=self.kwargs.get('cat'))
        print(res)
        print(self.kwargs)
        return{"products":res}

@method_decorator(dec,name="dispatch") 
class DetailsView(DetailView):
    template_name="details.html"
    queryset=products.objects.all()
    pk_url_kwarg='pid'
    context_object_name="product"
    def get_context_data(self,**kwargs: Any):
        context=super().get_context_data(**kwargs)
        pid=self.kwargs.get('pid')
        product=products.objects.get(id=pid)
        rev=Review.objects.filter(product=product)
        context["reviews"]=rev
        return context

@method_decorator(dec,name="dispatch") 
def addtocart(request,*args,**kwargs):
    pid=kwargs.get("pid")
    pro=products.objects.get(id=pid)
    user=request.user
    Cart.objects.create(product=pro,user=user)
    return redirect('uhome')

@method_decorator(dec,name="dispatch") 
class CartListView(ListView):
    template_name="cartlist.html"
    queryset=Cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user)
        return res

@method_decorator(dec,name="dispatch") 
class CartDeleteView(DeleteView):
    model=Cart
    success_url=reverse_lazy("lcart")
    template_name="deletecart.html"
    pk_url_kwarg="cid"

dec
def addreview(request,**kwargs):
    review=request.POST.get("rev")
    product_id=kwargs.get("pid")
    user=request.user
    product=products.objects.get(id=product_id)
    print(review,product_id)
    Review.objects.create(review=review,user=user,product=product)
    messages.success(request,"Review Added!!")
    return redirect("uhome")

@method_decorator(dec,name="dispatch")
class PlaceHolderView(TemplateView):
    template_name="placeholder.html"
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        cid=kwargs.get("cid")
        cart=Cart.objects.get(id=cid)
        product=cart.product
        user=request.user
        Orders.objects.create(product=product,user=user,address=address,phone=phone)
        Cart.status="Order Placed"
        cart.save()
        messages.success(request,"Order Placed Successfully!!")
        return redirect("uhome")

@method_decorator(dec,name="dispatch")   
class OrderListView(ListView):
    template_name="orderlist.html"
    queryset=Orders.objects.all()
    context_object_name="orders"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset

dec
def cancelorder(request,**kwargs):
    oid=kwargs.get('oid')
    order=Orders.objects.get(id=oid)
    Orders.order_status="Cancelled"
    order.save()
    #mail service
    # to_mail=request.user.email
    # msg=f"Order for the product {order.product.title} is cancelled successfully!!Check your email account for more details!"
    # from_mail="arjunmvbabu@gmail.com"
    # subject="Order Cancellation Confirmed"
    # send_mail(subject,msg,from_mail,[to_mail])
    return redirect('orl')


