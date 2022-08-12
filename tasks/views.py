from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.
# TODO: Add search bar
# TODO: Add pagination
# TODO: Style pages


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):  # TODO: Should not be able to create tasks for other users.
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks-view')


class TaskEditView(LoginRequiredMixin, UpdateView):  # TODO: Should not be able to edit tasks of other users.
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks-view')
    template_name = 'tasks/task_edit_form.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):  # TODO: Should not be able to delete tasks of other users.
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks-view')
