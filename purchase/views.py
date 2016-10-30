from django.shortcuts import render_to_response, render, HttpResponseRedirect
from models import TVPAl
from django.db.models import Sum
from forms import PForm


def party_trial(request):
    form = PForm()
    if request.method == 'POST':
        print('-'*30)
        form = PForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            date_from = data['date_from'].strftime("%Y-%m-%d")
            date_to = data['date_to'].strftime("%Y-%m-%d")
            print(date_from, date_to)

            # select party_id, sum(db), sum(cr)  from v_p_al where inv_date between date_from and date_to group by party_id
            party_trial = TVPAl.objects.values('party_id').filter(inv_date__range=(date_from, date_to)).annotate(db=Sum('db')).annotate(cr=Sum('cr'))
            context = {
                'form': form,
                'party': party_trial
            }
            return render(request, 'party_trial.html', context)
        else:
            return HttpResponseRedirect('/party_trial/')
    else:
        context = {
                'form': form
            }
        return render(request, 'party_trial.html', context)


def party_trial_detail(request, party_id, date_from, date_to):
    # select
    # party_id, inv_id, inv_date, particulars, db, cr
    # from v_p_al
    # where
    # party_id = p_party_id
    form = PForm()
    if request.method == 'POST':
        print('-'*30)
        print('this is the detail post')
        form = PForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            date_from = data['date_from'].strftime("%Y-%m-%d")
            date_to = data['date_to'].strftime("%Y-%m-%d")
            print(date_from, date_to)

            party_trial = TVPAl.objects.filter(party_id=party_id).filter(inv_date__range=(str(date_from), str(date_to)))
            context = {
                'form': form,
                'party': party_trial
            }
            return render(request, 'party_trial_detail.html', context)
        else:
            return HttpResponseRedirect('/party_trial/')
    else:

        party_trial = TVPAl.objects.filter(party_id=party_id).filter(inv_date__range=(str(date_from), str(date_to)))
        context = {
            'form': form,
            'party': party_trial
        }

        return render(request, 'party_trial_detail.html', context)


def party_trial_detail_w(request, party_id):
    # select
    # party_id, inv_id, inv_date, particulars, db, cr
    # from v_p_al
    # where
    # party_id = p_party_id
    form = PForm()
    if request.method == 'POST':
        print('-'*30)
        print('this is the detail post')
        form = PForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            date_from = data['date_from'].strftime("%Y-%m-%d")
            date_to = data['date_to'].strftime("%Y-%m-%d")
            print(date_from, date_to)

            party_trial = TVPAl.objects.filter(party_id=party_id).filter(inv_date__range=(str(date_from), str(date_to)))
            context = {
                'form': form,
                'party': party_trial
            }
            return render(request, 'party_trial_detail.html', context)
        else:
            return HttpResponseRedirect('/party_trial/')
    else:

        party_trial = TVPAl.objects.filter(party_id=party_id)
        context = {
            'form': form,
            'party': party_trial
        }

        return render(request, 'party_trial_detail.html', context)

