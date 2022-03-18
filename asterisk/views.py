import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from asterisk.models import PushReg, PushAck
from django.conf import settings


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


def send_push(request):
    from_user = request.GET.get("from")
    to_user = request.GET.get("to")
    try:
        push_reg = PushReg.objects.get(SIPUsername=to_user)
        device_token = push_reg.PushKey

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + settings.FCM_SERVER_KEY,
        }
        push_ack = PushAck()
        push_ack.SIPUsername = to_user
        push_ack.CallFrom = from_user
        push_ack.Ack = False
        push_ack.save(force_insert=True)
        body = {
            'to': device_token,
            'data': {
                'pushId': push_ack.id,
                'callFrom': from_user
            },
            'priority': 'high'
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
        print(response.text)
        return HttpResponse(push_ack.id)
    except PushReg.DoesNotExist:
        return HttpResponse(0)


def ack_push(request):
    pk = request.GET.get("id")
    push_ack = PushAck.objects.get(pk=pk)
    push_ack.Ack = True
    push_ack.save(force_update=True)
    return HttpResponse(push_ack.Ack)


def check_push(request):
    pk = request.GET.get("id")
    push_ack = PushAck.objects.get(pk=pk)
    return HttpResponse(push_ack.Ack)
