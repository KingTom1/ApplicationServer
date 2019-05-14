from ApplicationServerApp.models import User
from django.http import JsonResponse
import hashlib,time

def md5(username):
    now  = str(time.time())
    md5_obj= hashlib.md5(bytes(username,encoding='utf8'))
    md5_obj.update(bytes(now,encoding='utf8'))
    return md5_obj.hexdigest()


def Login(request):
    data = {
        'code': 1000,
        'status': 1,
        'error': 0,
    }
    try:
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        # 从数据库中获取表数据对象
        results = User.objects.filter(name=username,password=password)
        print(results)
        if results:
            token = md5(username)
            data['token']=token
        else:
            data['error']=1
            data['status']=0
            data['message']='用户名或者密码错误'
    except:
        data['error']=1
        data['status']=0
        data['message']='异常'
    return JsonResponse(data)