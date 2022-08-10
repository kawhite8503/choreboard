from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Chore

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chores_index(request):
  chores = Chore.objects.all()
  return render(request, 'chores/index.html', { 'chores': chores})

class ChoreCreate(CreateView):
  model = Chore
  fields = '__all__'
  success_url = '/chores/'