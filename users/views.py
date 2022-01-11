from django.shortcuts import render
from django.views.generic import ListView
from . import models


class UsersListView(ListView):
    model = models.User
    template_name = 'users/all_users.html'
    context_object_name = 'users'
