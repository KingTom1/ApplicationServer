from django.db import models

# Create your models here.
# 用户
class User(models.Model):
    class Meta:
        db_table = '用户'

    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='昵称', null=False)
    accountNumber = models.CharField(max_length=50, verbose_name='账户', null=False)
    password = models.CharField(max_length=200, verbose_name='密码', null=False)
    status = models.CharField(max_length=5, verbose_name='状态', null=False)
    createTime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # role=models.ManyToManyField('Role', verbose_name='用户拥有的角色', blank=True)
    # def __repr__(self):
    #     return "{} {}".format(self.name, self.password)
    #
    # _str_ = __repr__