from django.shortcuts import render,redirect
from .models import Planta
from .forms import PlantaForm,RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def galeria(request):
    return render(request, 'galeria.html')

def plantas(request):
    plantas = Planta.objects.raw('Select * from plantas_planta')
    datos={
        'plantitas':plantas
    }
    return render(request, 'plantas.html', datos)

@login_required
def crear(request):
    if request.method=="POST":
        planta_form =  PlantaForm(request.POST,request.FILES) #OBJETO TIPO FORMULARIO
        if planta_form.is_valid():
             planta_form.save()                 #INSERTAR PRODUCTO DE JARDINERIA
             return redirect('plantas')
        else:
             planta_form=PlantaForm()
        return render(request, 'crear.html', {'planta_form':planta_form})

@login_required
def eliminar(request, id):
    plantaEliminada = Planta.objects.get(codigo=id) # SELECT * FROM PLANTA WHERE codigo=id
    plantaEliminada.delete()
    return redirect ('plantas')

@login_required
def modificar(request, id):
    plantaModificada=Planta.objects.get(codigo=id)
    datos= {
        'form' : PlantaForm(instance=plantaModificada) # 'form' : OBJETO QUE LLEGA A TEMPLATE MODIFICAR
    }
    if request.method=='POST':
        formulario = PlantaForm(data=request.POST, instance=plantaModificada)
        if formulario.is_valid:
            formulario.save()
            return redirect('plantas')
    return render(request, 'modificar.html', datos)

def registrar(request):
    data= {
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],
                              password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        data["form"]=formulario
    return render(request, 'registration/register.html',data)

def contacto(request):
    return render(request, 'contacto.html')

def sesion(request):
    return render(request, 'sesion.html')