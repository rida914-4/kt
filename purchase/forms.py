from django import forms
from models import Company, Party


class PForm(forms.Form):
    date_from = forms.DateField(widget=forms.TextInput(attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1', 'aria-describedby': 'inputSuccess2Status'}), required=False)
    date_to = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left', 'id': 'single_cal2','aria-describedby': 'inputSuccess2Status'}), required=False)

    combo_final = ([('0'*20, 'Select Party')])
    items = Party.objects.all().values_list('party_id', 'party_name')
    combo_final.extend(items)
    comp_name = forms.ChoiceField(choices=combo_final, widget=forms.Select(attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': True, 'null': True, 'required': False}))

