from InvitationApp.resource import InvitationResource, MeetingResource
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from .utils import send_invitation
from .utils import get_meeting_name
# Register your models here.


class InvitationAdmin(ImportExportModelAdmin):
    resource_class = InvitationResource
    list_display = ['name', 'company', 'position', 'phone', 'email', 'city', 'note', 'confirm_number', 'is_sent', 'audit_status']

    actions = ['pass_audit', 'cancel_audit', 'send_sms']

    def pass_audit(self, request, queryset):
        for invitation in queryset:
            invitation.audit_status = True
            invitation.save()


    pass_audit.short_description = "审核通过"
    pass_audit.type = 'success'
    pass_audit.icon = 'el-icon-view'

    def cancel_audit(self, request, queryset):
        for invitation in queryset:
            invitation.audit_status = False
            invitation.save()

    cancel_audit.short_description = "取消审核"
    cancel_audit.type = 'danger'
    cancel_audit.icon = 'el-icon-close'

    def send_sms(self, request, queryset):
        # 请在后台确认会议号后，修改下面数字
        meeting = get_meeting_name(1)
        invitations = queryset.filter(audit_status=True)
        for invitation in invitations:
            print(meeting.name)
            print(invitation.confirm_number)
            # 调用发送短信接口
            body = send_invitation(meeting, invitation)
            print(body)
            if body.get("Code") == "OK":
                invitation.is_sent = True
                invitation.save()


    send_sms.short_description = "短信通知"
    send_sms.type = 'success'
    send_sms.icon = 'el-icon-chat-dot-square'

class MeetingAdmin(ImportExportModelAdmin):
    resource_class = MeetingResource
    list_display = ['id', 'name', 'date', 'place']

admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Meeting, MeetingAdmin)

admin.site.site_title = "佳研研讨会服务"
admin.site.site_header = "佳研研讨会服务"
admin.site.index_title = "佳研研讨会服务"