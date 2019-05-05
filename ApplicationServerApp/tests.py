from django.test import TestCase
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','applicationserver.settings')
django.setup()
# Create your tests here.
from ApplicationServerApp.models import User
# c1 = User('',name='yangjian',accountNumber='123',password='123456',status='1',createTime='2019-4-1')
user = User()
print(user)
user.name = 'lc'
user.accountNumber = '123'
user.password = '123456'
user.status = '1'
user.createTime = '2019-05-04'
user.save()
# c1.save()
