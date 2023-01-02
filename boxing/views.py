from django.shortcuts import render

# Create your views here.

def boxing(request):
    context = { 'title' : 'Boxing'}
    return render(request, 'boxing.html', context)
