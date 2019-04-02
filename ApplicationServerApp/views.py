from django.shortcuts import render

# Create your views here.
from ApplicationServerApp.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers

@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User(name=request.GET.get('add_user'),accountNumber='123',password='123456',status='1',createTime='2019-4-1')
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        # 从数据库中获取表数据对象
        users = User.objects.filter()
        # json.loads(serializers.serialize("json", users))讲数据对象转换成json字符串
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)