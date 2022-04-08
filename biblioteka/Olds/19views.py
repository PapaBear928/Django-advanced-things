from django.shortcuts import render
from django.http import HttpResponse
from .signals import main_signal
from .models import Autor

def main(request):
	main_signal.send(sender=Autor, imie="Bob")
	return HttpResponse("To jest nasza glowna strona")
