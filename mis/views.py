from django.shortcuts import render_to_response, render
from models import Party, TVPAl
from forms import PForm
from django.db.models import Sum
# Create your views here.



def mis(request):
    asset_db = Party.objects.all()
    form = PForm

    context = {
        'assets': asset_db
    }

    return render(request, 'mis.html', {'form': form})
