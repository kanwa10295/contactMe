from django.conf.urls import url

from . import views
urlpatterns = [url(r'^index/$',views.index, name='index'),
url(r'^adduser/$',views.addUser, name='addUser'),
                url(r'^deluser/$',views.delUser, name='delUser'),
url(r'^showuser/$',views.showUsers, name='ShowUser'),
url(r'^showdetail/$',views.showDetail, name='ShowDetail'),
url(r'^tempcontact/$',views.tempContact, name='tempcontact'),
               url(r'^(?P<username>[a-z]+)/$',views.detail,name='detail'),
url(r'^view-contact/(?P<contactt_list>\w+)/$',views.view_contact, name='view_contact'),
               url(r'^add-contact/(?P<contact_list>\w+)/$', views.add_contact, name='add_contact'),

               ]