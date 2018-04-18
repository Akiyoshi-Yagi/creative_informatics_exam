from django.http import HttpResponse,Http404,HttpResponseRedirect
from . models import Member, Task
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .forms import MemberForm,TaskForm
from django.template.response import TemplateResponse



def member_index(request):

    all_members=Member.objects.all()



    return render(request,'dowhat/member_index.html',{'all_members':all_members})


def member_detail(request,member_id):
    try:
        member  = Member.objects.get( pk= member_id)
    except:
        raise Http404('Member does not exist.')

    return render(request,'dowhat/member_detail.html',{'member':member})


def member_edit(request,member_id):

    eachmember = get_object_or_404(Member,id = member_id)
    if request.method =='POST':
        form = MemberForm(request.POST,instance=eachmember)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_index'))

    else:
        form = MemberForm(instance=eachmember)
        return TemplateResponse(request,'dowhat/member_edit.html',{'form':form,'member':eachmember})


def member_add(request):

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_index'))

    else:
        form = MemberForm()
        return TemplateResponse(request, 'dowhat/member_add.html', {'form': form,})



def member_delete(request,member_id):

    eachmember = get_object_or_404(Task, id=member_id)

    if request.method == 'POST':

        eachmember.delete()

        return redirect('member_index')

    else:


        return TemplateResponse(request, 'dowhat/member_delete.html', {'task': eachmember})












def task_index(request):

    all_tasks=Task.objects.all()



    return render(request,'dotask/task_index.html',{'all_tasks':all_tasks})


def task_detail(request,task_id):
    try:
        task  = Task.objects.get( pk= task_id)
    except:
        raise Http404('Task does not exist.')

    return render(request,'dotask/task_detail.html',{'task':task})


def task_edit(request,task_id):

    eachtask = get_object_or_404(Task,id = task_id)
    if request.method =='POST':
        form = TaskForm(request.POST,instance=eachtask)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_index'))

    else:
        form = TaskForm(instance=eachtask)
        return TemplateResponse(request,'dotask/task_edit.html',{'form':form,'task':eachtask})


def task_add(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_index'))

    else:
        form = TaskForm()
        return TemplateResponse(request, 'dotask/task_add.html', {'form': form,})


def task_delete(request,task_id):

    eachtask = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':

        eachtask.delete()

        return redirect('task_index')

    else:


        return TemplateResponse(request, 'dotask/task_delete.html', {'task': eachtask})





















