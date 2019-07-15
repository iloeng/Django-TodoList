# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import ToDo
from .forms import ToDoPostForm
from django.contrib.auth.models import User

# def all_list(request):
#     todo_list = ToDo.objects.all()
#     content = {'todos': todo_list}
#     return render(request, 'index.html', content)
#
#
# def todo_create(request, owner):
#     if request.method == "POST":
#         todo_post_form = ToDoPostForm(data=request.POST)
#         if todo_post_form.is_valid():
#             new_todo = todo_post_form.save(commit=False)
#             new_todo.owner = owner
#             new_todo.save()
#             return redirect("index")
#         else:
#             return HttpResponse("表单内容有误，请重新填写！")


def todolist(request):
    todolist = ToDo.objects.filter(status='No')
    finishtodos = ToDo.objects.filter(status='Yes')
    dicts = {'todolist': todolist, 'finished': finishtodos}
    return render(request, 'index.html', dicts)


def todofinish(request, id=''):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'No':
        todo.status = 'Yes'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No')
    return render(request, 'simple-todo.html', {'todolist': todolist})


def todoback(request, id=''):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'Yes':
        todo.status = 'No'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No')
    return render(request, 'simple-todo.html', {'todolist': todolist})


def tododelete(request, id=''):
    todo = ToDo.objects.get(id=id)
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(flag='No')
    return render(request, 'simple-todo.html', {'todolist': todolist})


def add_todo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        # priority = request.POST['priority']
        # owner = User.objects.get(id='1')
        owner = request.POST['owner']

        todo = ToDo(owner=owner, content=atodo.strip(), status='No')
        todo.save()
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        return render(request, 'index.html', {'todolist': todolist, 'finishtodos': finishtodos})

    else:
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        return render(request, 'index.html', {'todolist': todolist, 'finishtodos': finishtodos})


def update_todo(request, id=''):
    if request.method == 'POST':
        print('ddd')
        atodo = request.POST['todo']
        # priority = request.POST['priority']
        # owner = User.objects.get(id='1')
        owner = request.POST['owner']

        todo = ToDo(owner=owner, ontent=atodo, status='No')
        todo.save()
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        return render(request, 'show-todo.html',
                      {'todolist': todolist, 'finishtodos': finishtodos})

    else:
        todo = ToDo.objects.get(todo_id=id)
        return render(request, 'update.html', {'todo': todo})
