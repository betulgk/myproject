from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
]
