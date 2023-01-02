from django.shortcuts import render

# Create your views here.

def lift(request):
    context = {}
    return render(request, 'lift.html', context)