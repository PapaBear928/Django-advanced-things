from django.http import HttpResponse
from .signals import main_signal
from .models import Autor, Ksiazka
from .forms import OurForm
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render



def our_form(request):
	if request.method == 'POST':
		form = OurForm(request.POST)
		if form.is_valid():
			print("Is valid")
	else:
		form = OurForm()
	return render(request, 'our_form.html', {'form': form})


def main(request):
	main_signal.send(sender=Autor, imie="Bob")
	autor = {'imie': 'Walty', 'nazwisko': 'Whity'}
	ksiazka = {'tytul': 'WW', 'rok_wydania': 2111}
	add_to_db(autor,ksiazka)
	return HttpResponse("To jest nasza glowna strona")


def sending_mail(request):
	if request.method == 'POST':
		if request.POST.get('email', False):
			email = request.POST['email']
			message = ' testing mail' + email
			ksiazki = Ksiazka.objects.all()
			for ksiazka in ksiazki:
				message += '\n\r' + ksiazka.tytul
			try:
				send_mail("See this site",
	                message,
	                email,
                    ['bisip46031@whwow.com'],
	                fail_silently=False)
				messages.success(request, "Mail was send")
			except:
				messages.error(request, "Error")


	return render(request, 'email_form.html')

	#return HttpResponse("Mail has sent")


def add_to_db(autor,ksiazka):
		nowy_autor = Autor.objects.create(**autor)
		nowa_ksiazka = Ksiazka(**ksiazka)
		nowa_ksiazka.autor = nowy_autor
		nowa_ksiazka.save()