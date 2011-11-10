# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from models import Programmer
from pair_stair.pair_wall.models import Pair

def stairs_display(request):
    # get all programmers from data base
    pairs = Pair.objects.all()
    programmers = Programmer.objects.all()
    return render_to_response('pairstairs.html', {'programmers': programmers, 'pairs': pairs},
                          context_instance=RequestContext(request))

def add_pair_count(request, first_member, second_member):
    pairs = Pair.objects.all()
    for pair in pairs:
        if first_member == pair.first_member and second_member == pair.second_member:
            pair.count +=1
            pair.save()
    return redirect(stairs_display)


def create_pairs(newProgrammer, programmers):
    for programmer in programmers:
        pair = Pair(first_member=newProgrammer, second_member=programmer.name, count=0)
        pair.save()

def pairstairs_add_programmer(request):
    if request.method == 'POST':
        newProgrammer = request.POST['programmer']
        programmers = Programmer.objects.all()
        programmer_names = map(lambda x: x.name, programmers)
        if newProgrammer not in programmer_names:
            create_pairs(newProgrammer, programmers)
            Programmer(name = newProgrammer).save()
        return redirect(stairs_display)
    return render_to_response('addprogrammer.html')