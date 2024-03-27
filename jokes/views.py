from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

# Create your views here.
from .models import Joke

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