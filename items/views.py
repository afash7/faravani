# items/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm

@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('items:item_list')
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {'form': form})

@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_form.html', {'form': form})

@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/item_detail.html', {'item': item})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('items:item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})



# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Item
# from .forms import ItemForm

# @login_required
# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'items/item_list.html', {'items': items})

# @login_required
# def item_create(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.owner = request.user
#             item.save()
#             return redirect('item_list')
#     else:
#         form = ItemForm()
#     return render(request, 'items/item_form.html', {'form': form})

# @login_required
# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return render(request, 'items/item_detail.html', {'item': item})

# @login_required
# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('item_list')
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'items/item_form.html', {'form': form})

# @login_required
# def item_delete(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('item_list')
#     return render(request, 'items/item_confirm_delete.html', {'item': item})

# @login_required
# def item_update(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('item_detail', pk=item.pk)  # آدرس مناسب را به جای 'item_detail' قرار دهید
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'items/item_form.html', {'form': form})
