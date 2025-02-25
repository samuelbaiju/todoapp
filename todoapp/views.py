from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TASK
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class Tasklist(LoginRequiredMixin,ListView):
    model=TASK
    context_object_name="tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(task_name__icontains=search_input)
        context['search_input']=search_input
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model=TASK
    context_object_name='task'
    template_name='todoapp/task_det.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model=TASK
    fields=['task_name','task_description','task_status']
    success_url=reverse_lazy('tasks')
    template_name='todoapp/tasknew.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskEdit(LoginRequiredMixin,UpdateView):
    model=TASK
    fields=['task_name','task_description','task_status']
    success_url=reverse_lazy('tasks')
    template_name='todoapp/tasknew.html'

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=TASK
    success_url=reverse_lazy('tasks')
    context_object_name='task'
    template_name='todoapp/delete_task.html'
    
class CustomLoginView(LoginView):
    template_name='todoapp/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterView(FormView):
    template_name='todoapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterView, self).get(*args, **kwargs)

    

    