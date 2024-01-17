from django.db import models


class Questao(models.Model):
    DIFICULDADE_CHOICES = (
        (1, 'Fácil'),
        (2, 'Médio'),
        (3, 'Difícil'),
    )


    OPCAO_CHOICES = (
        ('A', 'Opção A'),
        ('B', 'Opção B'),
        ('C', 'Opção C'),
        ('D', 'Opção D'),
        ('E', 'Opção E'),
    )

    
    dificuldade = models.IntegerField(choices=DIFICULDADE_CHOICES)
    materia = models.TextField()
    texto_questao = models.TextField()
    opcao_a = models.TextField()
    opcao_b = models.TextField()
    opcao_c = models.TextField()
    opcao_d = models.TextField()
    opcao_e = models.TextField()
    correta = models.CharField(max_length=1, choices=OPCAO_CHOICES)
    
    def __str__(self):
        return self.materia

    
class Prova(models.Model):
    titulo = models.TextField(blank=True)
    curso = models.TextField()
    questoes = models.ManyToManyField(Questao)

    
    def __str__(self):
        return self.curso
    

class Candidato(models.Model):
    nome = models.TextField()
    email = models.EmailField(max_length=254)
    telefone = models.TextField()

    def __str__(self):
        return self.nome


class Resposta(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    escolha = models.CharField(max_length=1)
    
    def __str__(self):
        return self.candidato.nome

