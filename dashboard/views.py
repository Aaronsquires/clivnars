from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from simple_history.utils import update_change_reason
from django.template.loader import get_template

from django.db.models import F

from django.http import HttpResponse
from django.views.generic import View

import datetime
import csv

from django.contrib.auth.decorators import login_required

# from django.views.generic import (CreateView, DeleteView, ListView, UpdateView, DeleteView, TemplateView)
from django.views import generic

from .models import Product, Colours, Supplier, ProductBacklog

from .forms import ProductForm, RawProductForm, EditProductForm, AddColorsForm, ColoursForm, SupplierForm

from .utils import render_to_pdf


class ModalCreateView(generic.CreateView):
    model = Product
    fields = '__all__'
 
    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'stocklist/stocklist.html')


#
# Stocklist
#

# def stocklist_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form': form
#     }
#     return render(request, "stocklist/stocklist_create.html", context)


class stocklist_createview(generic.CreateView):
    template_name = 'stocklist/stocklist_create.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('stocklist')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class stocklist_updateview(generic.UpdateView):
    template_name = 'stocklist/stocklist_edit.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('stocklist')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class stocklist_listview(generic.ListView):
    template_name = 'stocklist/stocklist.html'
    queryset = Product.objects.all()


class stocklist_deleteview(generic.DeleteView):
    template_name = 'stocklist/stocklist_delete.html'
    form_class = ProductForm
    success_url = reverse_lazy('stocklist')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    def get_success_url(self):
        return reverse('stocklist')


def selection(request):
    return render(request, "selection.html", {})



#
# INVENTORY
#

class inventory_listview(generic.ListView):
    template_name = 'inventory/inventory.html'
    queryset = Product.objects.all()


# def edit_inventory_item_view(request, id):
#     obj = Product.objects.get(id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "inventory/inventory_edit.html", context)


class inventory_updateview(generic.UpdateView):
    template_name = 'inventory/inventory_edit.html'
    form_class = EditProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('inventory')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Settings View

class settings_detailview(generic.TemplateView):
    template_name = 'settings/settings.html'


# Colour Views

class colours_listview(generic.ListView):
    template_name = 'settings/colours/colour_listview.html'
    queryset = Colours.objects.all()


class colours_createview(generic.CreateView):
    template_name = 'settings/colours/colours_create.html'
    form_class = AddColorsForm
    queryset = Colours.objects.all()
    success_url = reverse_lazy('colours_listview')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class colour_item_updateview(generic.UpdateView):
    template_name = 'settings/colours/colours_edit.html'
    form_class = ColoursForm
    queryset = Colours.objects.all()
    success_url = reverse_lazy('colours_listview')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Colours, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Supplier Views

class supplier_listview(generic.ListView):
    template_name = 'settings/suppliers/suppliers_listview.html'
    queryset = Supplier.objects.all()


class supplier_createview(generic.CreateView):
    template_name = 'settings/suppliers/suppliers_create.html'
    form_class = SupplierForm
    queryset = Supplier.objects.all()
    success_url = reverse_lazy('suppliers_listview')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class supplier_item_updateview(generic.UpdateView):
    template_name = 'settings/suppliers/suppliers_edit.html'
    form_class = SupplierForm
    queryset = Supplier.objects.all()
    success_url = reverse_lazy('suppliers_listview')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Supplier, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class product_backlog(generic.ListView):
    template_name = 'settings/backlog/backlog_listview.html'
    # pylint: disable=no-member
    queryset = Product.history.all()



class GenerateLowStockPdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('print_pdf.html')
        objects = Product.objects.filter(quantity__lte=F('minquantity'))
        data = {
            'user': request.user,
            'currentdate': datetime.date.today(),
            'objects': objects,
            'title': 'Out of Stock Items',
            'reportDetails': 'Items Out of Stock',
            'pdfID': 'lowStockItems'
        }
        pdf = render_to_pdf('print_pdf.html', data)
        html = template.render(data)
        return HttpResponse(pdf, content_type='application/pdf')

class PrintAllStocksAsPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('print_pdf.html')
        objects = Product.objects.all()
        data = {
            'user': request.user,
            'currentdate': datetime.date.today(),
            'objects': objects,
            'title': 'Current Stock Items',
            'reportDetails': 'Items Currently in Stocklist',
            'pdfID': 'stocklistItems'
        }
        pdf = render_to_pdf('print_pdf.html', data)
        html = template.render(data)
        return HttpResponse(pdf, content_type='application/pdf')

class PrintAllInventoryItemsPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('print_pdf.html')
        objects = Product.objects.all()
        data = {
            'user': request.user,
            'currentdate': datetime.date.today(),
            'objects': objects,
            'title': 'Current Inventory Levels',
            'reportDetails': 'Current Inventory Levels',
            'pdfID': 'inventoryStock'
        }
        pdf = render_to_pdf('print_pdf.html', data)
        html = template.render(data)
        return HttpResponse(pdf, content_type='application/pdf')


def export_products_as_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="StockList.csv"'

    products = Product.objects.all()
    writer = csv.writer(response)
    writer.writerow(['code', 'description', 'quantity'])

    for product in products:
        writer.writerow([
            product.code,
            product.description,
            product.supplier,
            product.quantity,
            product.minquantity
        ])

    return response
