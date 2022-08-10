from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chore, Household

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')


@login_required
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

@login_required
def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  return render(request, 'chores/detail.html', { 'chore': chore})


class ChoreCreate(LoginRequiredMixin, CreateView):
  model = Chore
  fields = '__all__'
  success_url = '/chores/'

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class ChoreUpdate(LoginRequiredMixin, UpdateView):
  model = Chore
  fields = ['name', 'location', 'details', 'day_of_week', 'assigned_to']

class ChoreDelete(LoginRequiredMixin, DeleteView):
  model = Chore
  success_url = '/chores/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('chores_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
