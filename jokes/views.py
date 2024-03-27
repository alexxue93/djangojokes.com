from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
from .models import Joke

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

class JokeDetailView(DetailView):
    model = Joke
    
class JokeListView(ListView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')