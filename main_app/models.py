from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


DAYS = (
  ('SUN', 'Sunday'),
  ('MON', 'Monday'),
  ('TUE', 'Tuesday'),
  ('WED', 'Wednesday'),
  ('THU', 'Thursday'),
  ('FRI', 'Friday'),
  ('SAT', 'Saturday'),
)

class Household(models.Model):
  hh_code = models.CharField(max_length=250)

  def __str__(self):
    return self.hh_code


class Chore(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  details = models.TextField(
    max_length=250,
    blank=True
    )
  day_of_week = models.CharField(
    max_length=3,
    choices=DAYS,
    default=DAYS[0][0]
    )
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
  hh_code = models.ForeignKey(Household, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} was assigned to {self.assigned_to}'

  def get_absolute_url(self):
    return reverse('chores_detail', kwargs={'chore_id': self.id})