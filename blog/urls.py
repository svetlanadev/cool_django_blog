from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^edit/(?P<post_id>[0-9]+)/post/$', views.edit_post, name='edit_post'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
        ]