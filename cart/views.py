from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request,tot=0,count=0,cart_items=None):
     
     try:
         ct=cartlist.objects.get(cart_id=c_id(request))
         ct_items=items.objects.filter(cart=ct,active=True)
         for i in ct_items:
             tot += (i.prodt.price * i.quan)
             count += i.quan
     except ObjectDoesNotExist:
        pass
     return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prodt=products.objects.get(id=product_id)
    s_item=products.objects.get(id=product_id)
    # prodt.stock-=1
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        s_item.stock-=1
        ct.save()
    try:
        c_items=items.objects.get(prodt=prodt,cart=ct)
        # print(c_items.prodt.name)
        # s_item.stock-=1
        if c_items.quan < c_items.prodt.stock:
            s_item.stock-=1
            # print(s_item.stock)
            c_items.quan+=1
            # print(c_items.quan)
            c_items.save()
            s_item.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prodt,quan=1,cart=ct)
        s_item.stock-=1
        c_items.save()
        s_item.save()
    return redirect('cartDetails')    
    
def  min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prodt=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prodt,cart=ct)
    s_item=products.objects.get(id=product_id)
    if c_items.quan >1:
        c_items.quan-=1
        s_item.stock+=1
        print(s_item.stock)
        print(c_items.quan)
        s_item.save()
        c_items.save()
    else:
        s_item.stock+=1
        s_item.save()
        c_items.delete()
    return redirect('cartDetails')

def cart_delete(request,product_id):
     ct=cartlist.objects.get(cart_id=c_id(request))
     prodt=get_object_or_404(products,id=product_id)
     s_item=products.objects.get(id=product_id)
     c_items=items.objects.get(prodt=prodt,cart=ct)
     s_item.stock+=c_items.quan
     s_item.save()
     c_items.delete()
     return redirect('cartDetails')