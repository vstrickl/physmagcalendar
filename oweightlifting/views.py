from django.shortcuts import render

# Create your views here.

def lift(request):
    context = { 'title' : 'Olympic Weightlifting'}
    return render(request, 'lift.html', context)