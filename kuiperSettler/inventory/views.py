from django.shortcuts import render
from django.shortcuts import redirect
from .models import Inventory,Item

def view_inventory(request):
    # Assuming the user is authenticated
    user_inventory = Inventory.objects.filter(user=request.user)
    return render(request, 'inventory.html', {'user_inventory': user_inventory})



def add_item_to_inventory(request):
    # Create a new item and add it to the user's inventory
    new_item = Item.objects.create(name='New Item', description='Description of new item', base_price=10, category='Category', weight=0)
    Inventory.objects.create(user=request.user, item=new_item, quantity=1, equipped=False, total_weight=0)
    return redirect('view_inventory')