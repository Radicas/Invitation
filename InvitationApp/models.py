from django.db import models
from django.db.models.expressions import F

# Create your models here.
class Invitation(models.Model):
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField("姓名", max_length=32, default="")
    company = models.CharField("公司名", max_length=32, default="")
    position = models.CharField("职位", max_length=32, default="")
    phone = models.CharField("手机", max_length=12, default="", unique=True)
    email = models.CharField("邮箱", max_length=32, default="")
    city = models.CharField("城市", max_length=32, default="")
    note = models.CharField("备注", max_length=32, default="")
    confirm_number = models.CharField("确认号", max_length=32, default="")
    is_sent = models.BooleanField("是否发送", default=False)
    msg_status = models.CharField("短信状态", default="", max_length=128)
    audit_status = models.BooleanField("审核状态", default=False)
    def __str__(self):
        return self.name

class Meeting(models.Model):
    name = models.CharField("会议名", max_length=32, default="", unique=True)
    date = models.DateField("日期")
    place = models.CharField("地点", max_length=32, default="", )

    def __str__(self):
        return self.name