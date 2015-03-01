from django.conf.urls import patterns, include, url
from django.contrib import admin
from addOpportunity import views as views2
import captcha
import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opportunitiesSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
# testing, remove next line later
#    url(r'post/form_upload.html', views.IndexView.as_view()), 

    url('^$',views.HomeView.as_view(), name='home'),
    url(r'^add/',include('addOpportunity.urls')),
    url(r'^addOpportunity/',include('addOpportunity.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^viewAdded/', views.HomeView.as_view(), name='index'),
    url(r'^viewAdded/(?P<pk>\d+)', views2.DetailView.as_view(), name='detail'),
    url(r'^viewAdded/', views2.post_list, name='index'),
    url(r'^post/form_upload.html$',
        'addOpportunity.views.add', name = 'post_form_upload'),
)
