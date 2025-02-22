from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import UserModel
from .forms import UserForm


class CreateUser(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = "users/registration.html"
    success_url = "/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect(self.success_url)
