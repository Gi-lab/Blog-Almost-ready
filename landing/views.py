from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.

def home(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'home.html')

def listar(request):
    listar_frase = Aluno.objects.all(ativo=True)
    args = {
        'listar_frase': listar_frase
    }
    return render(request, 'lista.html', args)

def deletar(request):
    item = Aluno.objects.get(id=id)
    if item is not none:
        item.ativo = false 
        item.save()
        return redirect('aluno/listar')
        return render(request, 'lista.html')
