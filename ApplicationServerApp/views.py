from django.shortcuts import render

# Create your views here.
from ApplicationServerApp.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
import pandas as pd
from django.core import serializers

@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User(name=request.GET.get('add_user'),accountNumber='123',password='123456',status='1',createTime='2019-4-1')
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 0
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_user(request):
    response = {}
    arr =[]
    try:
        # 从数据库中获取表数据对象
        users = User.objects.filter()
        jsonStr = json.loads(serializers.serialize("json", users))
        for i in range(len(jsonStr)):
            namei = jsonStr[i]['fields']['name']
            arr.insert(i,namei)
        response['list'] = arr
        response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 0
    return JsonResponse(response)

@require_http_methods(["GET"])
def Login(request):
    response = {}
    try:
        username = request.GET.get('username')
        password = request.GET.get('password')
        # 从数据库中获取表数据对象
        username = User.objects.filter(name=username)
        password = User.objects.filter(password=password)
        if username and password:
            # json.loads(serializers.serialize("json", users))讲数据对象转换成json字符串
            jsonStr = json.loads(serializers.serialize("json", username))
            for i in range(len(jsonStr)):
                response['list'+str(i)] = jsonStr[i]['fields']
                response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 0
    return JsonResponse(response)