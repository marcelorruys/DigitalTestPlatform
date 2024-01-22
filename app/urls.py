from django.urls import path, include

from .views import index, index_questao, criar_questao, deletar_questao, index_prova, menu, editar_prova, add_questao, editar_questao_get, editar_questao_post, criar_prova, add_prova, deletar_prova, index_dashboard, capturar_informacoes, candidato_prova, candidato_finalizada, confirmar_deletar_prova, confirmar_deletar_questao


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    path('menu/', menu, name='menu'),
   
     
    path('questoes/', index_questao, name='index_questao'),
    path('questoes/criar', criar_questao, name='criar_questao'),
    path('questoes/criar/add', add_questao, name='add_questao'),
    path('questoes/editar/<int:id>', editar_questao_get, name='editar_questao'),
    path('questoes/update/<int:id>', editar_questao_post, name='update_questao'),
    path('questoes/confirmar/<int:id>', confirmar_deletar_questao, name='confirmar_deletar_questao'),
    path('questoes/deletar/<int:id>', deletar_questao, name='deletar_questao'),


    path('prova/', index_prova, name='index_prova'),
    path('prova/criar', criar_prova, name='criar_prova'),
    path('prova/criar/add', add_prova, name='add_prova'),
    path('prova/editar/<int:id>', editar_prova, name='editar_prova'),
    path('prova/confirmar/<int:id>', confirmar_deletar_prova, name='confirmar_deletar_prova'),
    path('prova/deletar/<int:id>', deletar_prova, name='deletar_prova'),

    
    path('dashboard/', index_dashboard, name='index_dashboard'),


    path('', index, name='index'),
    path('candidato/provas', capturar_informacoes, name='capturar_informacoes'),
    path('candidato/prova/<int:id>', candidato_prova, name='candidato_prova'),
    path('candidato/finalizada/', candidato_finalizada, name='candidato_finalizada'),
]
