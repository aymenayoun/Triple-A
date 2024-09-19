from django.shortcuts import render
from django.db.models import Sum
from expenses.models import Expenses  
from userincome.models import UserIncome 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')
def compare_income_expenses(request):
    # total income for the logged-in user
    total_income = UserIncome.objects.filter(owner=request.user).aggregate(total_income=Sum('amount'))['total_income'] or 0

    #total expense for the logged-in user
    total_expenses = Expenses.objects.filter(owner=request.user).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

    #difference (+ ou -)
    balance = total_income - total_expenses

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    }

    return render(request, 'my_account/comparison.html', context)

