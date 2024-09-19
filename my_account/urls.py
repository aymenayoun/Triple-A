from django.urls import path
from . import views

urlpatterns = [
    path('compare/', views.compare_income_expenses, name='compare-income-expenses'),
]
