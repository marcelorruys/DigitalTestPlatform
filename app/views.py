from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Questao, Prova, Candidato, Resposta

from random import choice


@login_required
def menu(request):
    return render(request, 'menu/index.html')


@login_required
def index_questao(request):
    questoes = Questao.objects.all()
    context = {
        'questoes' : questoes
    }
    return render(request, 'questao/index.html', context)


@login_required
def criar_questao(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        peso = request.POST.get('peso')
        dificuldade = request.POST.get('dificuldade')
        materia = request.POST.get('materia')
        texto_questao = request.POST.get('texto_questao')
        opcao_a = request.POST.get('opcao_a')
        opcao_b = request.POST.get('opcao_b')
        opcao_c = request.POST.get('opcao_c')
        opcao_d = request.POST.get('opcao_d')
        opcao_e = request.POST.get('opcao_e')
        correta = request.POST.get('correta')
        Questao.objects.create(titulo=titulo, peso=peso, dificuldade=dificuldade, materia=materia, texto_questao=texto_questao, opcao_a=opcao_a, opcao_b=opcao_b, opcao_c=opcao_c, opcao_d=opcao_d, opcao_e=opcao_e, correta=correta)
        return redirect(index_questao)
    else:
        return render(request, 'questao/criar.html')
    
    
def add_questao(request):
    return render(request, 'questao/adicionado.html')
    

@login_required
def editar_questao_get(request, id):
    questao = Questao.objects.get(id=id)
    
    context = {
        'questao' : questao
    }
    return render(request, 'questao/editar.html', context)


def editar_questao_post(request, id):
    questao = Questao.objects.get(id=id)
    questao.titulo = request.POST.get('titulo')
    questao.peso = request.POST.get('peso')
    questao.dificuldade = request.POST.get('dificuldade')
    questao.materia = request.POST.get('materia')
    questao.texto_questao = request.POST.get('texto_questao')
    questao.opcao_a = request.POST.get('opcao_a')
    questao.opcao_b = request.POST.get('opcao_b')
    questao.opcao_c = request.POST.get('opcao_c')
    questao.opcao_d = request.POST.get('opcao_d')
    questao.opcao_e = request.POST.get('opcao_e')
    questao.correta = request.POST.get('correta')
    questao.save()
    return redirect(index_questao)


@login_required
def deletar_questao(request, id):
    questao = Questao.objects.get(id=id)
    questao.delete()
    return redirect(index_questao)


@login_required
def index_prova(request):
    provas = Prova.objects.all()
    context = {
        'provas' : provas
    }
    return render(request, 'prova/index.html', context)


@login_required
def criar_prova(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        curso = request.POST.get('curso')
        qnt_questoes = int(request.POST.get('quantidade'))

        questoes_total = Questao.objects.all()
        questoes_sorteadas = list()
        for i in range(qnt_questoes):
            questoes_sorteadas.append(choice(questoes_total))
        prova = Prova.objects.create(titulo=titulo, curso=curso) 
        prova.questoes.set(questoes_sorteadas)
        return redirect(index_prova) 
    else:
        return render(request, 'prova/criar.html')


@login_required
def add_prova(request):
    return render(request, 'prova/adicionado.html')


@login_required
def editar_prova(request, id):
    if request.method == 'POST':
        prova = Prova.objects.get(id=id)
    else:
        prova = Prova.objects.get(id=id)
        if request.method == 'POST':
            prova.delete()
            return redirect(index_prova)
        else:
            context = {
                'prova' : prova
            }
            return render(request, 'prova/editar.html', context)


@login_required
def deletar_prova(request, id):
    prova = Prova.objects.get(id=id)
    prova.delete()
    return redirect(index_prova)


@login_required
def index_dashboard(request):
    return render(request, 'dashboard/index.html')


def index(request):
    print(request.session)
    return render(request, 'candidato/index.html')


def capturar_informacoes(request):
    if request.method=="POST":
        request.session['nome'] = request.POST.get('nome')
        request.session['email'] = request.POST.get('email')
        request.session['telefone'] = request.POST.get('telefone')

        return redirect(candidato_provas_index)
    else:
        return render(request, 'candidato/index.html')
    

def candidato_provas_index(request):
    if request.method == 'POST':
        request.session['prova.id'] = request.POST.get('')
    else:
        provas_visiveis = Prova.objects.get(status=True)
        context = {
            'provas' : provas_visiveis
        }
        return render(request, 'candidato/provas.html', context)
    
def candidato_prova(request):
    return 