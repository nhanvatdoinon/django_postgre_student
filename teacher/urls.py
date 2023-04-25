from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import Home
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('teacher/',login_required(Home.as_view()),name = 'teacher'),
        path('addteacher/',views.add_teacher,name='addteacher'),
]