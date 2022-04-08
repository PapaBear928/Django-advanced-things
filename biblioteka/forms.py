from django import forms
from django.core.validators import MaxValueValidator
from .validators import validate_rok

class OurForm(forms.Form):
	name = forms.CharField(label='imie', max_length=21, validators=[MaxValueValidator(21, message='Something')])
	surname = forms.CharField(label='nazwisko', max_length=21)

#	def clean_name(self):
#		cleaned_data = super(OurForm, self).clean()
#		name = self.cleaned_data.get('name')
#		if name > 21 :
#			raise forms.ValidationError('Message')
#		return name'''


#	def cleaned(self):
#		cleaned_data = super(OurForm, self).clean()
#		name = cleaned_data.get('name')
#		if name > 21:
#			raise forms.ValidationError('Message')
#		return name


	def cleaned(self):
		cleaned_data = super(OurForm, self).clean()
		return validate_rok(cleaned_data.get('rok'))

