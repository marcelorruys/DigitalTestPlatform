from django.urls import path, include

from .views import index, index_questao, criar_questao, deletar_questao, index_prova, menu, detalhes_prova, add_questao, editar_questao_get, editar_questao_post


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', index, name='index'),
    
    
    path('menu/', menu, name='menu'),
    
    path('questoes/', index_questao, name='index_questao'),
    path('questoes/criar', criar_questao, name='criar_questao'),
    path('questoes/criar/add', add_questao, name='add_questao'),
    path('questoes/editar/<int:id>', editar_questao_get, name='editar_questao'),
    path('questoes/update/<int:id>', editar_questao_post, name='update_questao'),
    path('questoes/deletar/<int:id>', deletar_questao, name='deletar_questao'),

    path('prova/', index_prova, name='index_prova'),
    path('prova/criar', criar_questao, name='criar_prova'),
    path('prova/detalhes/<int:id>', detalhes_prova, name='editar_prova'),
    
    path('questoes/', index_questao, name='index_dashboard'),
]
