# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Trailers(models.Model):

    #__Trailers_FIELDS__
    trailer_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Trailers_FIELDS__END

    class Meta:
        verbose_name        = _("Trailers")
        verbose_name_plural = _("Trailers")


class Orders(models.Model):

    #__Orders_FIELDS__
    order_id = models.CharField(max_length=255, null=True, blank=True)
    ord_status = models.CharField(max_length=255, null=True, blank=True)

    #__Orders_FIELDS__END

    class Meta:
        verbose_name        = _("Orders")
        verbose_name_plural = _("Orders")



#__MODELS__END
