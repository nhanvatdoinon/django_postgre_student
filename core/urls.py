from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import Home, add_student
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('student/',Home.as_view(),name = 'student'),
    path('add/',views.add_student,name='add'),
    path('delete/<str:id>',views.delete_student,name='delete'),
    path('edit/<int:id>/',views.edit_student,name='edit'),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('search/', views.search, name='search'),
    #path('filter/',views.filterstudent,name='filter')
]
