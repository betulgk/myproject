
from django.contrib import admin
from django.urls import path
from post.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('created', HomeView.as_view(), name='post_new'),
]