from django.core.exceptions import ValidationError

def validate_rok(value):
	if value > 2020:
		raise ValidationError('message')
	return value