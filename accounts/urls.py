from django.conf.urls import url
from accounts.views import login_view

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
]
