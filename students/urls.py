from django.contrib import admin
from django.urls import path
from students.views import Students,Groups,Contact_admin




urlpatterns = [
    path('',Students.students_list,name='home'),
    path('students/add/', Students.students_add,name='students_add'),
    path('students/<int:sid>/edit/',Students.students_edit,name='students_edit'),
    path('students/<int:sid>/delete/',Students.students_delete,name='students_delete'),

    path('groups/', Groups.groups_list, name='groups'),
    path('groups/add/',Groups.groups_add,name='groups_add'),
    path('groups/(<int:gid>/edit/',Groups.groups_edit,name='groups_edit'),
    path('groups/(<int:gid>/delete/',Groups.groups_delete,name='groups_delete'),

    path('contact-admin/', Contact_admin.contact_admin,name='contact_admin'),
    ]
