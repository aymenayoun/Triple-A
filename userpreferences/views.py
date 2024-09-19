from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages 

def index(request):
    # Ensure that the user settings are created before trying to get them
    user_settings, created = UserPreference.objects.get_or_create(user=request.user)
    
    # getting the data from the JSON file
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        currency_data = [{'name': i, 'value': j} for i, j in data.items()]

    if request.method == 'GET':
        return render(request, 'preferences/index.html', {'currencies': currency_data, 'user_settings': user_settings})
    else:
        currency = request.POST['currency']
        user_settings.currency = currency
        user_settings.save()
        messages.success(request, 'Currency changed successfully')
        return render(request, 'preferences/index.html', {'currencies': currency_data, 'user_settings': user_settings})
