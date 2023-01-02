from django.shortcuts import render

# Create your views here.

def studio(request):
    context = { 'title' : 'Martial Arts & Dance Studio'}
    return render(request, 'studio.html', context)