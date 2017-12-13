from django import forms
from models import *
from capstone.models import *
from django.contrib.auth.models import User

class KPIForm(forms.Form):
	kpi1 = forms.DecimalField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'kpi1'}))
	kpi2 = forms.DecimalField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'kpi2'}))
	kpi3 = forms.DecimalField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'kpi3'}))
	kpi4 = forms.DecimalField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'kpi4'}))
	kpi5 = forms.DecimalField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'kpi5'}))
	extra_field_count = forms.CharField(widget = forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		extra_fields = kwargs.pop('extra', 0)

		if not extra_fields:
			extra_fields = 0
		super(KPIForm, self).__init__(*args, **kwargs)
	    	self.fields['extra_field_count'].initial = extra_fields

	        for index in range(int(extra_fields)):
	            # generate extra fields in the number specified via extra_fields
	            self.fields['extra_field_{index}'.format(index=index)] = \
	                forms.DecimalField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'kpi{index}'.format(index=index)}))

	def clean(self):
		cleaned_data = super(KPIForm, self).clean()
		kpi1 = cleaned_data.get('kpi1')
		kpi2 = cleaned_data.get('kpi2')
		kpi3 = cleaned_data.get('kpi3')
		kpi4 = cleaned_data.get('kpi4')
		kpi5 = cleaned_data.get('kpi5')

		if kpi1 < 1.0 or kpi2 < 1.0 or kpi3 < 1.0 or kpi4 < 1.0 or kpi5 < 1.0:
			raise forms.ValidationError("KPI must be greater than or equal to 1")

		if kpi1 > 6.0 or kpi2 > 6.0 or kpi3 > 6.0 or kpi4 > 6.0 or kpi5 > 6.0:
			raise forms.ValidationError("KPI must be less than or equal to 6")
		return cleaned_data
