from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.students_list,name='home'),
    path('students/add/', views.students_add,name='students_add'),
    path('students/<int:sid>/edit/',views.students_edit,name='students_edit'),
    path('students/<int:sid>/delete/',views.students_delete,name='students_delete'),

    path('groups/', views.groups_list, name='groups'),
    path('groups/add/',views.groups_add,name='groups_add'),
    path('groups/(<int:gid>/edit/',views.groups_edit,name='groups_edit'),
    path('groups/(<int:gid>/delete/',views.groups_delete,name='groups_delete'),
    ]
