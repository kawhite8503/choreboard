from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('chores/', views.chores_index, name='chores_index'),
  path('chores/<int:chore_id>/', views.chores_detail, name='chores_detail'),
  path('chores/create', views.ChoreCreate.as_view(), name='chores_create'),
  path('chores/<int:pk>/update/', views.ChoreUpdate.as_view(), name='chores_update'),
  path('chores/<int:pk>/delete/', views.ChoreDelete.as_view(), name='chores_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]