from django.conf.urls import url
from django.contrib.auth import login
from accounts.views import signup

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', signup, name='signup'),

]