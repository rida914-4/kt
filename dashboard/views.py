from django.shortcuts import render, render_to_response

# Create your views here.


def dashboard(request):
    context = {}
    return render_to_response('dashboard.html', context)
