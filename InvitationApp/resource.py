from import_export import resources
from .resource import *
from .models import *
from django.db import models
import tablib
import collections


class InvitationResource(resources.ModelResource):
    class Meta:
        model = Invitation


class MeetingResource(resources.ModelResource):
    class Meta:
        model = Meeting

