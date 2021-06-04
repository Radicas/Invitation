import json
from utils import AliyunClient
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from .models import Meeting, Invitation

ACCESS_KEY = "LTAI5tFKEgMRxPmu4QHYyPXW"
ACCESS_KEY_SECRET = "mJ3er04XdNkviloqR0T1GGeSuTlx6F"


_client = AliyunClient.create_client(ACCESS_KEY, ACCESS_KEY_SECRET)


def get_client():
    return _client

def get_meeting_name(id):
    meeting = Meeting.objects.get(id=id)
    return meeting

def send_invitation(meeting: Meeting, invitation: Invitation):
    client = get_client() 
    data = {
        "name": invitation.name,
        "confirmNumber": invitation.confirm_number,
        "date": str(meeting.date),
        "meeting": meeting.name,
        "place": meeting.place
    }
    send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
        phone_numbers=invitation.phone,
        sign_name='佳研实业',
        template_code='SMS_218037258',
        template_param=json.dumps(data)
    )
    # 复制代码运行请自行打印 API 的返回值
    resp = client.send_sms(send_sms_request)
    body = resp.to_map()['body']
    return body
    