# django
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
# custom
from utils import create_random_string, Resp
from utils.regex import PHONE_REGEX
from .models import *
from .utils import get_meeting_name
# third party
from .tasks import test_celery

def test_c():
    test_celery.delay().get()

class SignUpView(View):
    # @csrf_exempt
    # def get(self, request):
    #     title = "ANSYS 芯片-封装-电路板协同仿真研讨会报名表"
    #     return render(request, "invitation/sign_up.html", {"title": title})
    @csrf_exempt
    def post(self, request):
        name = request.POST.get('name')
        company = request.POST.get('company')
        position = request.POST.get('position')
        phone  = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        note = request.POST.get('note')
        
        if not PHONE_REGEX.match(phone):
            resp = Resp(code=200, msg="请输入正确的手机号", data={})
        elif not all([name, company, position, phone, email, city]):
            resp = Resp(code=200, msg="请填写所有信息", data={})
        elif Invitation.objects.filter(phone=phone).count() != 0:
            resp = Resp(code=200, msg="您已报名，请勿重复报名")
        else:
            confirm_number = create_random_string()
            meeting = get_meeting_name(1)
            invitation = Invitation(
                name=name, 
                company=company,
                position=position,
                phone=phone,
                email=email,
                city=city,
                note=note,
                confirm_number=confirm_number,
                meeting=meeting)
            # 需求变动，不需要直接发送了，如果需要直接发送，把下面这行两行去掉
            invitation.save()
            resp = Resp(code=200, msg="感谢您的报名，请等待负责人审核，如报名成功，我们将短信通知您，谢谢！")
            # try:
            #     body = send_invitation(meeting, invitation)
            #     print(body)
            #     invitation.msg_status = str(body)
            #     if body.get("Code") == 'OK':
            #         invitation.is_sent=True
            #         resp = Resp(code=200, msg="恭喜您报名成功！请注意查收短信。")
            #     else:
            #         resp = Resp(code=200, msg="恭喜您报名成功！")
            #     invitation.save()
            # except Exception as e:
            #     resp = Resp(code=200, msg="抱歉，服务器出错了～")
            #     print(e)
        return JsonResponse(resp.dict())

