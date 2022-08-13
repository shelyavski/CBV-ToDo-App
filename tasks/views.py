from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.
# TODO: Add pagination
# TODO: Style pages


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_completed=False).count()

        search_input = self.request.GET.get('search_bar') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input
            )
        context['search_input'] = search_input
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks-view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks-view')
    template_name = 'tasks/task_edit_form.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks-view')
