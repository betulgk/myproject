from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post.views import HomeView, JsonTestView, LoginHomeView
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    url(r'^newestposts/(?P<pk>\d+)$', JsonTestView.as_view()),
    url(r'^accounts/', include('accounts.urls')),
    path('home/', LoginHomeView.as_view(), name='login-home'),

]

urlpatterns += static(
       settings.STATIC_URL,
       document_root=settings.STATIC_ROOT
   )