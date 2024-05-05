from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')

    bag = request.session.get('bag', {})
    if size:
        bag_item = bag.setdefault(item_id, {'items_by_size': {}})
        items_by_size = bag_item['items_by_size']
        if size in items_by_size:
            items_by_size[size] += quantity
            message = f'Updated size {size.upper()} {product.name} quantity to {items_by_size[size]}'
        else:
            items_by_size[size] = quantity
            message = f'Added size {size.upper()} {product.name} to your bag'
    else:
        bag[item_id] = bag.get(item_id, 0) + quantity
        message = f'Updated {product.name} quantity to {bag[item_id]}'

    messages.success(request, message)
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')

    bag = request.session.get('bag', {})
    if size:
        bag_item = bag.setdefault(item_id, {'items_by_size': {}})
        items_by_size = bag_item['items_by_size']
        if quantity > 0:
            items_by_size[size] = quantity
            message = f'Updated size {size.upper()} {product.name} quantity to {items_by_size[size]}'
        else:
            del items_by_size[size]
            if not items_by_size:
                bag.pop(item_id)
            message = f'Removed size {size.upper()} {product.name} from your bag'
    else:
        if quantity > 0:
            bag[item_id] = quantity
            message = f'Updated {product.name} quantity to {bag[item_id]}'
        else:
            bag.pop(item_id)
            message = f'Removed {product.name} from your bag'

    messages.success(request, message)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            message = f'Removed size {size.upper()} {product.name} from your bag'
        else:
            bag.pop(item_id)
            message = f'Removed {product.name} from your bag'

        messages.success(request, message)
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
