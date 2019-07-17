# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import ToDo
# from .forms import ToDoForm


def todolist(request):
    todolist = ToDo.objects.filter(status='No').order_by('-owner')
    finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
    # for todo in todolist:
    reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear}
    return render(request, 'index.html', dicts)


def finish_reappear(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if request.method == 'POST':
        if todo.status == 'No':
            invested = float(request.POST['investe'])
            todo.status = 'Yes'
            todo.finish = 'Yes'
            todo.invested_time = invested
            todo.save()
            todolist = ToDo.objects.filter(status='No').order_by('-owner')
            finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
            # for todo in todolist:
            reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
            unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
            dicts = {'todolist': todolist, 'finished': finishtodos,
                     'reappear': reappear, 'unreappear': unreappear}
            return render(request, 'index.html', dicts)
    todolist = ToDo.objects.filter(status='No').order_by('-owner')
    finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
    # for todo in todolist:
    reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear}
    return render(request, 'index.html', dicts)


def finish_unreappear(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if request.method == 'POST':
        if todo.status == 'No':
            invested = float(request.POST['invested'])
            todo.status = 'Yes'
            todo.finish = 'No'
            todo.invested_time = invested
            todo.save()
            todolist = ToDo.objects.filter(status='No').order_by('-owner')
            finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
            # for todo in todolist:
            reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
            unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
            dicts = {'todolist': todolist, 'finished': finishtodos,
                     'reappear': reappear, 'unreappear': unreappear}
            return render(request, 'index.html', dicts)
    todolist = ToDo.objects.filter(status='No').order_by('-owner')
    finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
    # for todo in todolist:
    reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear}
    return render(request, 'index.html', dicts)


def todoback(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if todo.status == 'Yes':
        todo.status = 'No'
        todo.finish = 'No'

        todo.invested_time = 0.0
        todo.save()
        todolist = ToDo.objects.filter(status='No').order_by('-owner')
        finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
        # for todo in todolist:
        reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
        unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
        dicts = {'todolist': todolist, 'finished': finishtodos,
                 'reappear': reappear, 'unreappear': unreappear}
        return render(request, 'index.html', dicts)
    todolist = ToDo.objects.filter(status='No')
    finishtodo = ToDo.objects.filter(status='Yes')
    return render(request, 'index.html', {'todolist': todolist, 'finished': finishtodo})


def tododelete(request, id):
    todo = ToDo.objects.get(todo_id=id)
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = ToDo.objects.filter(status='No').order_by('-owner')
    finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
    # for todo in todolist:
    reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear}
    return render(request, 'index.html', dicts)


def add_todo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        # priority = request.POST['priority']
        # owner = User.objects.get(id='1')
        owner = request.POST['owner']

        todo = ToDo(owner=owner, content=atodo.strip(), status='No', finish='No')
        todo.save()
        todolist = ToDo.objects.filter(status='No').order_by('-owner')
        finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
        # for todo in todolist:
        reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
        unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
        dicts = {'todolist': todolist, 'finished': finishtodos,
                 'reappear': reappear, 'unreappear': unreappear}
        return render(request, 'index.html', dicts)

    else:
        todolist = ToDo.objects.filter(status='No').order_by('-owner')
        finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
        # for todo in todolist:
        reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
        unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
        dicts = {'todolist': todolist, 'finished': finishtodos,
                 'reappear': reappear, 'unreappear': unreappear}
        return render(request, 'index.html', dicts)


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
        todo.invested_time = 0.0
        todo.save()
        todolist = ToDo.objects.filter(status='No')
        finishtodos = ToDo.objects.filter(status='Yes')
        # return render(request, 'index.html',
        #               {'todolist': todolist, 'finished': finishtodos})
        todolist = ToDo.objects.filter(status='No').order_by('-owner')
        finishtodos = ToDo.objects.filter(status='Yes').order_by('-resolve_time')
        # for todo in todolist:
        reappear = ToDo.objects.filter(status='Yes', finish='Yes').order_by('-resolve_time')
        unreappear = ToDo.objects.filter(status='Yes', finish='No').order_by('-resolve_time')
        dicts = {'todolist': todolist, 'finished': finishtodos,
                 'reappear': reappear, 'unreappear': unreappear}
        return render(request, 'index.html', dicts)

    else:
        todo = ToDo.objects.get(todo_id=id)
        return render(request, 'update.html', {'todo': todo})


def user_page(request, username):
    todolist = ToDo.objects.filter(status='No', owner=username)
    finishtodos = ToDo.objects.filter(status='Yes', owner=username)
    reappear = ToDo.objects.filter(status='Yes', finish='Yes', owner=username).order_by('-resolve_time')
    unreappear = ToDo.objects.filter(status='Yes', finish='No', owner=username).order_by('-resolve_time')
    dicts = {'todolist': todolist, 'finished': finishtodos,
             'reappear': reappear, 'unreappear': unreappear,
             'user': username}
    return render(request, 'user.html', dicts)
