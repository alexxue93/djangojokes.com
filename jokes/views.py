from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import JokeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from .models import Joke

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

class JokeDetailView(DetailView):
    model = Joke
    
class JokeListView(ListView):
    model = Joke

class JokeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Joke
    #fields = ['question', 'answer']
    form_class = JokeForm
    success_message = 'Joke created.'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    #fields = ['question', 'answer']
    form_class = JokeForm
    success_message = 'Joke updated.'
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user