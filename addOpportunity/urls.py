from django.conf.urls import patterns, url
from addOpportunity import views

urlpatterns = patterns('',
    url(r'^$', views.add, name = "add"),
#    url(r'^viewAdded', views.IndexView.as_view(), name='index'),
#    url(r'^post/form_upload.html', views.add, name='post_form_upload'),

#    url(r'^$add', views.add, name='post_form_upload'),

#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^$', views.add, name='post_form_upload'),
#    url(r'^$', views.index, name='index'),
)


