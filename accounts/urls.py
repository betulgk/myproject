from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # url(r'^login/$', login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

]
