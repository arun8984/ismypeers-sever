from django.shortcuts import render
from django.http import HttpResponse
from asterisk.models import PushReg


def home(request):
    return render(request, 'home.html')


def register_push(request):
    sip_username = request.GET.get("username")
    push_key = request.GET.get("key")
    try:
        push_reg = PushReg.objects.get(SIPUsername=sip_username)
        push_reg.PushKey = push_key
        push_reg.save(force_update=True)
    except PushReg.DoesNotExist:
        push_reg = PushReg()
        push_reg.PushKey = push_key
        push_reg.SIPUsername = sip_username
        push_reg.save(force_insert=True)

    return HttpResponse('Success')
