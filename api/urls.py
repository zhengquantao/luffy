from django.conf.urls import url, include
from api.views import course
from api.views import auths

urlpatterns = [
    # 方式一
    # url(r'^course/', course.CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/', course.CourseView.as_view())

    # 方式二
    url(r'^course/$', course.CourseView.as_view({'get': 'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retreice'})),
    url(r'^auth/$', auths.AuthView.as_view()),
    url(r'^micro/$', course.MicroView.as_view())


]