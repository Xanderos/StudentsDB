from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
     return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
     return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
     return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
     return HttpResponse('<h1>Delete Group %s</h1>' % gid)