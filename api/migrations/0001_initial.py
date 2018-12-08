# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-26 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='章节')),
                ('name', models.CharField(max_length=32, verbose_name='章节名称')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='课程名称')),
                ('course_img', models.CharField(max_length=64, verbose_name='课程图片')),
                ('level', models.IntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1, verbose_name='课程难易程度')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slogon', models.CharField(max_length=255, verbose_name='口号')),
                ('why', models.CharField(max_length=255, verbose_name='为什么要学')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('recommend_courses', models.ManyToManyField(related_name='rc', to='api.Course', verbose_name='推荐课程')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course', verbose_name='所属课程'),
        ),
    ]