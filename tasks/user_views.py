from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login


class UserLoginView(LoginView):
    model = User
    template_name = 'tasks/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks-view')


class UserRegisterView(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user-login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks-view')
        return super(UserRegisterView, self).get(*args, **kwargs)
