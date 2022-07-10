from django.contrib import messages
from django.shortcuts import render, redirect

import authentication.models
from authentication.models import account
from .models import Transaction
from datetime import date

# Create your views here.

def transaction_view(request):
    context = {}
    user = request.user
    userobj = account.objects.get(username=user)
    if request.method == "POST":
        amount = request.POST['amount']
        touser = request.POST['touser']

        temp = True
        try:
            account_obj = account.objects.get(username=touser)
        except authentication.models.account.DoesNotExist:
            temp = False

        if temp:
            today = date.today()
            date_send = today.strftime("%Y-%m-%d")
            trans = Transaction(date=date_send, from_user=user, to_user=touser, jocund=amount)
            trans.save()

            if not userobj.is_office:
                datasave_from = account.objects.get(username=user)
                datasave_from.balance = str(int(datasave_from.balance) - int(amount))
                datasave_from.save()

            datasave_to = account.objects.get(username=touser)
            datasave_to.balance = str(int(datasave_to.balance) + int(amount))
            datasave_to.save()

            return redirect('homepage')


        else:
            messages.warning(request, "UserId Does not exist !!")






    userData = account.objects.get(username=user)
    context['user'] = userData

    return render(request, 'transaction.html', context)



def request_view(request):
    return render(request, 'request.html', {})

