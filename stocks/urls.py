from django.urls import path
from django.contrib import admin

from django.contrib.auth.decorators import login_required


from .views import home

from accounts.views import login_view, register_view, logout_view
from dashboard import views

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),
    path('', home),

    # Accounts
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view, name='logout'),

    # Selections
    path('dashboard/selection/', login_required(views.selection), name='selection'),

    # Inventory
    path('dashboard/inventory/', login_required(views.inventory_listview.as_view()), name='inventory'),
    path('dashboard/inventory/edit/<int:id>', login_required(views.inventory_updateview.as_view()), name='inventory_edit'),


    # Settings
    path('dashboard/settings/', login_required(views.settings_detailview.as_view()), name='settings'),

    # Settings - Stocklist
    path('dashboard/settings/stocklist/', login_required(views.stocklist_listview.as_view()), name='stocklist'),
    path('dashboard/settings/stocklist/create', login_required(views.stocklist_createview.as_view()), name='stocklist_create'),
    path('dashboard/settings/stocklist/edit/<int:id>', login_required(views.stocklist_updateview.as_view()), name='stocklist_edit'),
    path('dashboard/settings/stocklist/delete/<int:id>', login_required(views.stocklist_deleteview.as_view()), name='stocklist_delete'),


    # Settings - Colours
    path('dashboard/settings/colours', login_required(views.colours_listview.as_view()), name='colours_listview'),
    path('dashboard/settings/colours/add/colour', login_required(views.colours_createview.as_view()), name='colours_createview'),
    path('dashboard/settings/colours/edit/colour/<int:id>', login_required(views.colour_item_updateview.as_view()), name='colours_editview'),

    # Settings - Suppliers
    path('dashboard/settings/supplier', login_required(views.supplier_listview.as_view()), name='suppliers_listview'),
    path('dashboard/settings/supplier/add/supplier', login_required(views.supplier_createview.as_view()), name='suppliers_createview'),
    path('dashboard/settings/supplier/edit/supplier/<int:id>', login_required(views.supplier_item_updateview.as_view()), name='suppliers_editview'),

    # Settings - Backlog
    path('dashboard/settings/backlog', login_required(views.product_backlog.as_view()), name='product_backlog'),

    # Exports 
    # CSV
    path('dashboard/export/', views.export_products_as_csv, name='export_products'),
    # PDF
    path('dashboard/print/LowStocks', views.GenerateLowStockPdf.as_view(), name='print_table_lowstock'),
    path('dashboard/print/all', views.PrintAllStocksAsPDF.as_view(), name='print_table_allstock'),
    path('dashboard/print/inventory', views.PrintAllInventoryItemsPDF.as_view(), name='print_table_inventory'),

    path('dashboard/settings/stocklist/MODALCREATE', login_required(views.ModalCreateView.as_view()), name='modal_create'),
]
