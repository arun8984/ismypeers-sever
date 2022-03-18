from enum import IntEnum

from django.db import models


class DeviceType(IntEnum):
    ANDROID = 1
    IOS = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class PushReg(models.Model):
    SIPUsername = models.CharField('Sip Username', max_length=20, blank=False, null=False, unique=True)
    PushKey = models.CharField('Push Key', max_length=250, blank=False, null=False)
    DeviceType = models.PositiveSmallIntegerField('Device Type', choices=DeviceType.choices(),
                                                  default=DeviceType.ANDROID)
    CreatedOn = models.DateTimeField('Created On', auto_now_add=True)
    UpdatedOn = models.DateTimeField('Updated On', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Push Registry'
        verbose_name_plural = "Push Registry"

    def __str__(self):
        return self.SIPUsername


class PushAck(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    SIPUsername = models.CharField('Sip Username', max_length=20, blank=False, null=False)
    Ack = models.BooleanField('Ack', default=False)
    CallFrom = models.CharField('Call From', max_length=20, blank=False, null=False)
    CreatedOn = models.DateTimeField('Created On', auto_now_add=True)
    UpdatedOn = models.DateTimeField('Updated On', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Push Ack'
        verbose_name_plural = "Push Ack"

    def __str__(self):
        return self.SIPUsername
