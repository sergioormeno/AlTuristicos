from django.shortcuts import render
from .models import Comuna, Establecimiento, Region, Provincia
from .forms import ContactForm

def index(request):
	#print(Region.objects.all())
	#for instance in Region.objects.all():
	#	print(instance)
	queryset = Region.objects.all()
	context = {
		"queryset": queryset
	}
	return render(request, "index.html",context)

def Comunas(request):

	queryset = Comuna.objects.all()
	context = {
		"queryset": queryset
	}
	return render(request, "comuna.html",context)

def Provincias(request):

	queryset = Provincia.objects.all()
	context = {
		"queryset": queryset
	}
	return render(request, "provincias.html",context)

def Establecimientos(request):

	queryset = Establecimiento.objects.all()
	context = {
		"queryset": queryset
	}
	return render(request, "establecimiento.html",context)

def Regiones(request):

	queryset = Region.objects.all()
	context = {
		"queryset": queryset
	}
	return render(request, "regiones.html",context)


def Acerca(request):

	return render(request, "acerca.html")


def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })

def sortr(request, reg_id2):
	queryset = Establecimiento.objects.all().filter(reg_id=reg_id2)
	context = {
		"queryset": queryset
	}
	return render(request, "sortr.html",context)

def sortc(request, com_id2):
	queryset = Establecimiento.objects.all().filter(com_id=com_id2)
	context = {
		"queryset": queryset
	}
	return render(request, "sortc.html",context)

def sortp(request,prov_id2):
	queryset = Establecimiento.objects.all().filter(prov_id=prov_id2)
	context = {
		"queryset": queryset
	}
	return render(request, "sortp.html",context)