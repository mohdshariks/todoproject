
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Tasks
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Tasklistview(ListView):
    model = Tasks
    template_name = 'home.html'
    context_object_name = 'task1'
class TaskDetailview(DetailView):
    model=Tasks
    template_name='details.html'
    context_object_name='tasks'
class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('name','priority','date')


    def get_success_url(self):
        return reverse_lazy('cvdetails',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cvbhome')
# Create your views here.
def add(request):
    task1 = Tasks.objects.all()
    if request.method=='POST':
        name=request.POST.get('task',)
        priority=request.POST.get('priority',)
        date=request.POST.get('date','')
        task=Tasks(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'task1':task1})
# def details(request):
#
#     return render(request,'details.html',)
def delete(request,taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Tasks.objects.get(id=id)
    forms=TodoForm(request.POST or None, instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':forms,'task':task})

