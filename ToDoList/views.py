# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import ToDo
from .forms import ToDoPostForm

USER = {
    '卢敏': 1,
    '孙贝': 2,
    '刘瑶': 3,
    '明倩': 4,
    '家斌': 5,
    '晓娟': 6,
    '碧莹': 7,
    '张真': 8
}
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
    todolist = ToDo.objects.filter(status='No').order_by('-owner')
    finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
    # for todo in todolist:
    reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear}
    return render(request, 'index.html', dicts)


def todofinish(request, id=''):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'No':
        todo.status = 'Yes'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No')
    return render(request, 'simple-todo.html', {'todolist': todolist})


def finish_reappear(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'No':
        todo.status = 'Yes'
        todo.finish = 'Yes'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No')
    finishtodo = ToDo.objects.filter(status='Yes')
    return HttpResponseRedirect('/')


def finish_unreappear(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'No':
        todo.status = 'Yes'
        todo.finish = 'No'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No')
    finishtodo = ToDo.objects.filter(status='Yes')
    return HttpResponseRedirect('/')


def todoback(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'Yes':
        todo.status = 'No'
        todo.finish = 'No'
        todo.save()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No')
    finishtodo = ToDo.objects.filter(status='Yes')
    return render(request, 'index.html', {'todolist': todolist, 'finished': finishtodo})


def tododelete(request, id):
    todo = ToDo.objects.get(todu_id=id)
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(flag='No')
    finishtodo = ToDo.objects.filter(flag='Yes')
    return render(request, 'index.html', {'todolist': todolist, 'finished': finishtodo})


def add_todo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        # priority = request.POST['priority']
        # owner = User.objects.get(id='1')
        owner = request.POST['owner']

        todo = ToDo(owner=owner, content=atodo.strip(), status='No', finish='No')
        todo.save()
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        return render(request, 'index.html', {'todolist': todolist, 'finishtodos': finishtodos})

    else:
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        return render(request, 'index.html', {'todolist': todolist, 'finishtodos': finishtodos})


def update_todo(request, id):
    if request.method == 'POST':
        # print('ddd')
        atodo = request.POST['todo']
        # priority = request.POST['priority']
        # owner = User.objects.get(id='1')
        owner = request.POST['owner']

        todo = ToDo.objects.get(todo_id=id)
        todo.owner = owner
        todo.content = atodo
        todo.status = 'No'
        todo.finish = 'No'
        todo.save()
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        # return render(request, 'index.html',
        #               {'todolist': todolist, 'finished': finishtodos})
        return HttpResponseRedirect('/')

    else:
        todo = ToDo.objects.get(todo_id=id)
        return render(request, 'update.html', {'todo': todo})


def user_page(request, username):
    # todos = ToDo.objects.filter(owner=username)
    todolist = ToDo.objects.filter(status='No', owner=username)
    finishtodos = ToDo.objects.filter(status='Yes', owner=username)
    reappear = ToDo.objects.filter(status='Yes', finish='Yes', owner=username).order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No', owner=username).order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear,
             'user': username}
    return render(request, 'user.html', dicts)
