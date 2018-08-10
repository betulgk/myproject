from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from post.views import HomeView, LoginHomeView, JsonTestView
from django.conf.urls import url
from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    url(r'^newestposts/(?P<pk>\d+)$', JsonTestView.as_view()),
    path('home/', LoginHomeView.as_view(), name='login-home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup),
    url(r'^logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
