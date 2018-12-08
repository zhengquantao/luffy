from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from api import models
import uuid


class AuthView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        ret = {'code': 1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        user = models.UserInfo.objects.filter(user=user, pwd=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名密码错误'
        else:
            # 如果登入成功 生成随机字符串
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user, defaults={'token': uid})
            ret['token'] = uid
        return Response(ret)
