from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Order, OrderItem

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('menu')
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

@login_required
def add_to_cart(request, item_id):
    menu_item = MenuItem.objects.get(id=item_id)
    order, created = Order.objects.get_or_create(user=request.user, is_completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, menu_item=menu_item)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('view_cart')  

@login_required
def view_cart(request):
    try:
        order = Order.objects.get(user=request.user, is_completed=False)
        items = order.items.all()
    except Order.DoesNotExist:
        items = []
    return render(request, 'cart.html', {'items': items})

@login_required
def place_order(request):
    try:
        order = Order.objects.get(user=request.user, is_completed=False)
        order.is_completed = True
        order.save()
        return render(request, 'order_success.html')
    except Order.DoesNotExist:
        return redirect('menu')

