from django.contrib import admin

from asterisk.models import PushReg, PushAck


class PushRegAdmin(admin.ModelAdmin):
    list_display = ['SIPUsername', 'DeviceType', 'CreatedOn', 'UpdatedOn']


class PushAckAdmin(admin.ModelAdmin):
    list_display = ['SIPUsername', 'CallFrom', 'Ack', 'CreatedOn', 'UpdatedOn']


admin.site.register(PushReg, PushRegAdmin)
admin.site.register(PushAck, PushAckAdmin)
