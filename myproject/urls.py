
from django.contrib import admin
from django.urls import path
from post.views import HomeView, JsonTestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('posts', JsonTestView.as_view(), name='jhome'),
]