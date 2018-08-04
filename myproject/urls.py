
from django.contrib import admin
from django.urls import path, include
from post.views import HomeView, JsonTestView
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    url(r'^newestposts/(?P<pk>\d+)$', JsonTestView.as_view()),
    url(r'^accounts/', include('accounts.urls')),
]
