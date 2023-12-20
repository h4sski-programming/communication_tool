from django.shortcuts import render, redirect, get_object_or_404

from .models import Team, Member
from .forms import TeamForm


def index(request):
    team_1 = Team.objects.get(name='Team_1')
    team_1_members = list(team_1.members.all())
    teams = Team.objects.all()
    aaabbb = Member.objects.get(name='aaa bbb')
    
    context = {
        'teams': teams,
        'team_1': team_1,
        'team_1_members': team_1_members,
        'aaabbb': aaabbb,
        }
    return render(request, 'index.html', context)



def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeamForm()
    
    context = {
        'form': form,
    }
    return render(request, 'create_team.html', context)



def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        pass
    else:
        # form = 1
        pass
    
    context = {
        'aaa': 1,
    }
    return (render, 'edit_team.html', context)



def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete_team()
    return redirect('index')