from django.urls import path, include

from .views import index, index_questao, criar_questao, deletar_questao, index_prova, menu, editar_prova, add_questao, editar_questao_get, editar_questao_post, criar_prova, add_prova, deletar_prova, index_dashboard, capturar_informacoes


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    path('menu/', menu, name='menu'),
   
     
    path('questoes/', index_questao, name='index_questao'),
    path('questoes/criar', criar_questao, name='criar_questao'),
    path('questoes/criar/add', add_questao, name='add_questao'),
    path('questoes/editar/<int:id>', editar_questao_get, name='editar_questao'),
    path('questoes/update/<int:id>', editar_questao_post, name='update_questao'),
    path('questoes/deletar/<int:id>', deletar_questao, name='deletar_questao'),


    path('prova/', index_prova, name='index_prova'),
    path('prova/criar', criar_prova, name='criar_prova'),
    path('prova/criar/add', add_prova, name='add_prova'),
    path('prova/editar/<int:id>', editar_prova, name='editar_prova'),
    path('prova/deletar/<int:id>', deletar_prova, name='deletar_prova'),

    
    path('dashboard/', index_dashboard, name='index_dashboard'),


    path('', index, name='index'),
    path('candidato/criar', capturar_informacoes, name='capturar_informacoes'),
]
