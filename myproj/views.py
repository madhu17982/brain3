from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from myproj.models import Item

def index(request):
    items= Item.objects.all()
    return render(request,'Brain/index.html',{
        'items': items,
                       
        })

def item_detail(request,id):
    try:
        item=Item.objects.get(id=id)
    except Item.DoesNotExit:
         raise Http404('This item does not exit')
    return render(request,'Brain/item_detail.html',{
        'item':item,
 })
