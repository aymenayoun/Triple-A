from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',views.index,name='income'),
    path('add-income',views.add_income,name='add-income'),
    path('edit-income/<int:id>',views.edit_income,name='edit-income'),
    path('delete-income/<int:id>/', views.delete_income, name='delete-income'),
    path('search-income/',csrf_exempt(views.search_income),name='search-income'),
    path('income_source_summary',views.income_source_summary,name='income_source_summary'),
    path('instats',views.stats_view,name='instats'),
    path('export-csv',views.export_csv,name='export-csv'),
    path('export-excel',views.export_excel,name='export-excel'),
    path('export-PDF',views.export_pdf,name='export-PDF'),
]