from django.db import models

# Create your models here.
class Team(models.Model):
    colapse = models.BooleanField(blank=False, default=True)
    name = models.CharField(max_length=250, unique=True, blank=False)
    # leader = models.
    
    def __str__(self) -> str:
        return self.name
    
    def delete_team(self):
        self.delete()
    
    
class Member(models.Model):
    # first_name = models.CharField(max_length=150, blank=False)
    # last_name = models.CharField(max_length=150, blank=False)
    name = models.CharField(max_length=250, unique=True, blank=False)
    email = models.EmailField(max_length=500, unique=True, blank=False)
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', blank=True)
    
    def __str__(self) -> str:
        return self.name
        # return f'{self.first_name} {self.last_name}'
