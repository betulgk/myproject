
from django.contrib import admin
from django.urls import path
from post.views import HomeView, EducationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('education/', EducationView.as_view(), name='education'),
    path('created', HomeView.as_view(), name='post_new'),
]