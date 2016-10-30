from django import forms
from models import Nom


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.acct_name


class PForm(forms.ModelForm):

    date_from = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}), required=False)
    date_to = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal2',
               'aria-describedby': 'inputSuccess2Status'}), required=False)

    class Meta:
        model = Nom
        exclude = ['o_bal', 'acct_type', 'fs_type', 'sub', 'test_name', 'comp_id', 'emp_id', 'acct_id']
        combo_final = ([('0'*20, 'Select One')])
        items = Nom.objects.all().values_list('acct_id', 'acct_name')
        combo_final.extend(items)
        widgets = {
            'acct_name': forms.Select(choices=combo_final, attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': True, 'null': True, 'required': False})
        }

