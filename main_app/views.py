from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Chore, Household

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chores_index(request):
  chores = Chore.objects.all()
  names = []
  new_list = []
  for chore in chores:
    names.append(chore.assigned_to)
  
  for name in names:
    if name not in new_list:
      new_list.append(name)
      print(new_list)

  return render( request, 'chores/index.html', { 'chores': chores, 'names': names, 'new_list': new_list, 'Household': Household})

def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  return render(request, 'chores/detail.html', { 'chore': chore})


class ChoreCreate(CreateView):
  model = Chore
  fields = '__all__'
  success_url = '/chores/'