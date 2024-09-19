from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',views.index,name='expenses'),
    path('add-expenses',views.add_expenses,name='add-expenses'),
    path('edit-expense/<int:id>',views.edit_expense,name='edit-expense'),
    path('delete-expense/<int:id>/', views.delete_expense, name='delete-expense'),
    path('search-expenses/',csrf_exempt(views.search_expenses),name='search-expenses'),
    path('expense_category_summary',views.expense_category_summary,name='expense_category_summary'),
    path('expstats',views.stats_view,name='expstats'),
    path('export-csv',views.export_csv,name='export-csv'),
    path('export-excel',views.export_excel,name='export-excel'),
    path('export-PDF',views.export_pdf,name='export-PDF'),
]