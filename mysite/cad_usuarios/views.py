from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password = senha)

        if user:
            login(request, user)
            return redirect('/sorveteria/')
        else:
            return render(request, 'login.html', {'ERROR':'Usuário ou senha invalidos!'})


def cadastro(request):
        if request.method == "GET":
                return render(request, "cadastro.html")
        
        else:
            if request.POST['username'] and request.POST['senha']:
                username = request.POST.get('username')
                senha = request.POST.get('senha')

                user = User.objects.filter(username=username).first()

                if user:
                    return render(request, 'cadastro.html', {'ERROR':'O Usuario já existe!'})
                    
                user = User.objects.create_user(username=username, password=senha)
                user.save()

                return render(request, 'cadastro.html', {'SUCCESS':'Cadastro efetuado!'})
            else:
                return render(request, 'cadastro.html', {'ERROR':'Preencha todos os campos!'})
            

def gerenciarUsuarios(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})

def apagarUsuario(request):
    users = User.objects.all()
    if request.method == "GET":
        return render(request, 'usuarios.html', {'users': users})
    else:
        if request.POST['username']:
            username = request.POST.get('username')
            if 'apagarUsuario' in request.POST:
                User.objects.get(username=username).delete()
                return render(request, 'usuarios.html', {'SUCCESS':'O Usuario foi apagado com sucesso!', 'users': users})
            else:
                user = User.objects.get(username=username)
                group = Group.objects.get(name="Gerenciador")
                if 'tornarGerenciador' in request.POST:
                    user.groups.add(group)
                    user.save()
                    return render(request, 'usuarios.html', {'SUCCESS':'O Usuario foi adicionado no cargo de Gerenciador!', 'users': users})
                else:
                    user.groups.remove(group)
                    user.save()
                    return render(request, 'usuarios.html', {'SUCCESS':'O Usuario foi removido do cargo de Gerenciador!', 'users': users})

        else:
            return render(request, 'usuarios.html', {'ERROR':'Escolha algum usuario!', 'users': users})