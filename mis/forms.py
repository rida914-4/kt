from django import forms
from models import Party, Company


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.acct_name


class PForm(forms.Form):
    date_from = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}), required=False)
    date_to = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal2',
               'aria-describedby': 'inputSuccess2Status'}), required=False)

    combo_final = ([('0'*20, 'Select One')])
    items = Company.objects.all().values_list('comp_id', 'comp_name')
    combo_final.extend(items)
    comp_name = forms.Select(choices=combo_final, attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': True, 'null': True, 'required': False})