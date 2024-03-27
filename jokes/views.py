from django.shortcuts import render
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Joke

class JokeDetailView(DetailView):
    model = Joke
    
class JokeListView(ListView):
    model = Joke