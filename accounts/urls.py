from django.conf.urls import url
from django.contrib.auth import login

from accounts import views
from post.views import HomeView

app_name = 'accounts'

urlpatterns = [
    # url(r'^login/$', login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

]
