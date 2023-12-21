from django.shortcuts import render, redirect, get_object_or_404

from .models import Team, Member
from .forms import TeamForm, MemberForm


def index(request):
    teams = Team.objects.all()
    
    context = {
        'teams': teams,
        }
    return render(request, 'index.html', context)


# # # # # # # # # # 
# # # # # # # # # # Team
# # # # # # # # # # 

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
        # print(f'Posting something')
        form = TeamForm(request.POST, instance=team)
        # print(request.POST['name'])
        if form.is_valid():
            form.save()
            return redirect('index')
        # return redirect('index')
    else:
        form = TeamForm(instance=team)
    
    context = {
        'form': form,
        'team': team,
    }
    return render(request, 'edit_team.html', context)


def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete_team()
    return redirect('index')


# # # # # # # # # # 
# # # # # # # # # # Member
# # # # # # # # # # 

def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MemberForm()
    
    context = {
        'form': form,
    }
    return render(request, 'create_member.html', context)


def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MemberForm(instance=member)
    
    context = {
        'form': form,
        'member': member,
    }
    return render(request, 'edit_member.html', context)


def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    member.delete_member()
    return redirect('index')