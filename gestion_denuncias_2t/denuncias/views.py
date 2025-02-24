from django.shortcuts import get_object_or_404, redirect, render
from .models import Denuncia, CATEGORIAS
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncias/index.html', {'denuncias': denuncias})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['titulo']
        descripcion = request.POST['descripcion']
        imagen = request.FILES['imagen']
        categoria = request.POST['categoria']
        denuncia = Denuncia(titulo=title, descripcion=descripcion, imagen=imagen, usuario=request.user, categoria=categoria)
        denuncia.save()
        return redirect('lista_denuncias')
    else:
        categorias = CATEGORIAS
        return render(request, 'denuncias/create.html', {'categorias': categorias})
    
@login_required
def edit(request, id):
    denuncia = get_object_or_404(Denuncia, id=id)
    categorias = CATEGORIAS
    if request.user == denuncia.usuario:
        if request.method == 'GET':
            return render(request, 'denuncias/edit.html', {'denuncia': denuncia, 'categorias': categorias})
        else:
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            try:
                if request.FILES['imagen']:
                    denuncia.imagen = request.FILES['imagen']
            finally:
                categoria = request.POST['categoria']
                denuncia.titulo = titulo
                denuncia.descripcion = descripcion
                denuncia.categoria = categoria
                denuncia.estado = request.POST['estado']
                denuncia.save()
                return redirect('lista_denuncias')

@login_required
def delete(request, id):
    denuncia = get_object_or_404(Denuncia, id=id)
    if request.user == denuncia.usuario:
        denuncia.delete()
    return redirect('lista_denuncias')