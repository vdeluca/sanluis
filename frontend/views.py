from django.shortcuts import render, get_object_or_404
from empleo.models import Postulante, Puesto

# Create your views here.
# Create your views here.
def home(request):
	titulo =  "titulo"
	postulantes = Postulante.objects.all()
	puestos = Puesto.objects.all()
	context = {"postulantes":postulantes,"titulo":titulo,"puestos":puestos}
	return render(request,"base.html",context)
