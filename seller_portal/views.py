from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seller, SellerProduct
from .forms import SellerProductForm

@login_required
def seller_dashboard(request):
    seller = Seller.objects.get(user=request.user)
    products = SellerProduct.objects.filter(seller=seller)
    return render(request, 'seller_portal/dashboard.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = SellerProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = Seller.objects.get(user=request.user)
            product.save()
            return redirect('seller_dashboard')
    else:
        form = SellerProductForm()
    return render(request, 'seller_portal/add_product.html', {'form': form})

def become_seller(request):
    return render(request, 'become_seller.html')
