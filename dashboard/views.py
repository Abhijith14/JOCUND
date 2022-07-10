from django.shortcuts import render
from authentication.models import account
from transaction.models import Transaction
import numpy as np
from collections import OrderedDict

# Create your views here.

def dash_view(request):
    context = {}
    user = request.user
    fullData = account.objects.all()

    user_dict = {}
    for data in fullData:
        if data.is_student:
            user_dict[data.username] = data.TE

    dictionary_keys = list(user_dict.keys())

    sorted_dict = {dictionary_keys[i]: sorted(user_dict.values())[i] for i in range(len(dictionary_keys))}

    trans_obj = Transaction.objects.all()

    trans_list = []

    for data in trans_obj:
        if str(data.from_user) == str(user) or str(data.to_user) == str(user):
            trans_list.append(data)

    print(trans_list)

    userData = account.objects.get(username=user)

    if userData.is_student:
        context['ranking'] = list(sorted_dict).index(str(userData.username))
    context['user'] = userData
    context['transaction'] = trans_list

    return render(request, 'dashboard.html', context)


