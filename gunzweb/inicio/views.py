from django.shortcuts import render, redirect

# Create your views here.
def inicio(request): #def es para hacer funciones. al hacerle una request la vuelves una views
	return render(request,'index.html')

def registro(request):
	variable='esto es una variable'
	v1 = 1
	v2 = 2
	v3 = v1+v2
	return render(request,'registro.html',locals())#locals sirve para mandarme todos los datos a registro.html