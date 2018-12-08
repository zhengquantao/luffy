from django.db import models

# Create your models here.

class Course(models.Model):
    """
    课程表
    """
    title = models.CharField(verbose_name='课程名称', max_length=32)
    course_img = models.CharField(verbose_name='课程图片', max_length=64)
    level_choices = (
        (1, '初级'),
        (2, '中级'),
        (3, '高级')
    )
    level = models.IntegerField(verbose_name='课程难易程度', choices=level_choices, default=1)

    def __str__(self):
        return self.title  # 让返回数时显示的数据


class CourseDetail(models.Model):
    """
    课程详细
    """
    course = models.OneToOneField(to='Course')
    slogon = models.CharField(verbose_name='口号', max_length=255)
    why = models.CharField(verbose_name='为什么要学', max_length=255)
    recommend_courses = models.ManyToManyField(verbose_name='推荐课程', to='Course', related_name='rc')  # 加反向关联字段 related_name='xx'

    def __str__(self):
        return "课程详细"+self.course.title


class Chapter(models.Model):
    """
    章节
    """
    num = models.IntegerField(verbose_name='章节')
    name = models.CharField(verbose_name='章节名称', max_length=32)
    course = models.ForeignKey(verbose_name="所属课程", to='Course')

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)

    def __str__(self):
        return self.user


class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo")
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.token
