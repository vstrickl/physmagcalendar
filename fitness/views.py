from django.shortcuts import render

# Create your views here.

def fitness(request):

    context = { 
        'title' : 'Fitness',
    }

    return render(request, 'fitness.html', context)