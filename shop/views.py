from django.shortcuts import render, get_object_or_404

from .models import Item


def list_item(request):
    list_of_item = Item.objects.all()
    return render(request, 'list_item.html', {'items': list_of_item})


def detail_item(request, item_id):
    detail_list = get_object_or_404(Item, id=item_id)
    return render(request, 'detail_item.html', {'items': detail_list})
