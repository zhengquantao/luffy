from api import models
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    """
    课程信息的类
    """
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
    """
    课程详情的类
    """
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