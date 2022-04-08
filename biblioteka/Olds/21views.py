from django.http import HttpResponse
from .signals import main_signal
from .models import Autor, Ksiazka
from django.core.mail import send_mail

def main(request):
	main_signal.send(sender=Autor, imie="Bob")
	autor = {'imie': 'Walty', 'nazwisko': 'Whity'}
	ksiazka = {'tytul': 'WW', 'rok_wydania': 2111}
	add_to_db(autor,ksiazka)
	return HttpResponse("To jest nasza glowna strona")


def sending_mail(request):

	send_mail("See this site",
	          "Test",
	          'nadawca@test.pl',
	          ['bisip46031@whwow.com'],
	          fail_silently=False)
	if request.method == 'POST':
		if request.POST.get('email', False):
			email = request.POST['email']
			message = ' testing mail'

	return render(request, 'email_form.html')

	#return HttpResponse("Mail has sent")


def add_to_db(autor,ksiazka):
		nowy_autor = Autor.objects.create(**autor)
		nowa_ksiazka = Ksiazka(**ksiazka)
		nowa_ksiazka.autor = nowy_autor
		nowa_ksiazka.save()