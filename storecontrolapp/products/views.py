from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Nome do produto"}
        )
    )
    quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={"placeholder": "Quantidade"}
        )
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "Descrição"}
        )
    )
    value = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={"placeholder": "Valor", "step": "0.1"}
        ),
        max_digits=8,
        decimal_places=2
    )
    barcode = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Código de barras"}
        )
    )

    class Meta:
        model = Product
        fields = ['title', 'quantity', 'description', 'value', 'barcode'] 
       

def product_list(request, template_name='products/product_list.html'):
    product = Product.objects.all()
    data = {}
    data['object_list'] = product
    return render(request, template_name, data)

def product_view(request, pk, template_name='products/product_detail.html'):
    product = get_object_or_404(Product, pk=pk)    
    return render(request, template_name, {'object':product})

def product_create(request, template_name='products/product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})

def product_update(request, pk, template_name='products/product_form.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})

def product_delete(request, pk, template_name='products/product_confirm_delete.html'):
    product = get_object_or_404(Product, pk=pk)    
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, template_name, {'object':product})
