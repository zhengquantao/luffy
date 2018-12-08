from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from rest_framework import serializers
from api.auth.auth import LuffyAuth


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")  # 得到level数字对应的文字
    class Meta:
        model = models.Course
        fields = ['id', 'title', 'course_img', 'level']  # '__all__' 全部数据

# class CourseDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CourseDetail
#         fields = '__all__'
#         depth = 2  # 根据关联字段找到表序列化2层（0-10）

class CourseDetailSerializer(serializers.ModelSerializer):
    # 以下这3种方法只适合one2one/foreignkey/choice
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')



    # many2many
    recommends = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    def get_recommends(self, obj):
        # 获取推荐的所有课程
        queryset = obj.recommend_courses.all()
        return [{'id': row.id, 'title': row.title} for row in queryset]

    def get_chapter(self, obj):
        # 获取推荐的所有章节
        queryset = obj.course.chapter_set.all()
        return [{'id': row.id, 'num': row.num, 'name': row.name} for row in queryset]


    class Meta:
        model = models.CourseDetail
        fields = ['why', 'title', 'img', 'level', 'course', 'slogon', 'recommends', 'chapter']  # 指定数据
        depth = 2

#  方法一
# class CourseView(APIView):
#     def get(self, request, *args, **kwargs):
        # ret = {
        #     'code': 1000,
        #     'data': [
        #         {"id": 1, "title": 'python全栈'},
        #         {"id": 2, 'title': 'Linux运维'},
        #         {"id": 3, 'title': '金融分析'}
        #     ]
        # }
        # return Response(ret)
# 方法一
        # ret = {'code': 1000, 'data': None}
        # try:
        #     pk = kwargs.get('pk')
        #     if pk:
        #         obj = models.Course.objects.filter(id=pk).first()
        #         # 序列化
        #         ser = CourseSerializer(instance=obj, many=False)
        #     else:
        #         queryset = models.Course.objects.all()
        #         # 序列化
        #         ser = CourseSerializer(instance=queryset, many=True)
        #     ret['data'] = ser.data
        # except Exception as e:
        #     ret['code'] = 1001
        #     ret['data'] = '获取失败'
        # return Response(ret)

# 方法二
# views
# APIView
# GenericAPIView

from rest_framework.viewsets import GenericViewSet, ViewSetMixin


class CourseView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取失败'
        return Response(ret)

    def retreice(self, request, *args, **kwargs):
        """
        个人信息接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            # 课程ID
            pk = kwargs.get('pk')
            # obj = models.Course.objects.filter(id=pk).first()  # 通过Course查询ID为pk的信息
            # ser = CourseSerializer(instance=obj, many=False)  # 序列化obj信息
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取失败'
        return Response(ret)

# def test(self, request, *args, **kwargs):
#     obj = models.Course.objects.filter(id=2).first()
#     print(obj.title)
#     print(obj.level)  # 得到的数字
#     print(obj.get_level_display())  # 得到的是对应文字
#     return Response('....')


class MicroView(APIView):
    authentication_classes = [LuffyAuth, ]  # 认证组件

    def get(self, request, *args, **kwargs):
        # token = request.query_params.get('token')
        # obj = models.UserToken.objects.filter(token=token)
        # if not obj:
        #     return Response('认证失败')
        print(request.user)
        print(request.auth)
        ret = {'code': 1000, 'title': '微职位'}
        return Response(ret)
