from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def usuarios (request):
    return render(request, 'usuarios.html')

def usuarios(request):
    user_list =[
    {"nome": "Ana Silva", "matricula": "202501", "idade": 20, "cidade": "São Paulo"},
    {"nome": "Bruno Costa", "matricula": "202502", "idade": 22, "cidade": "Rio de Janeiro"},
    {"nome": "Carla Mendes", "matricula": "202503", "idade": 19, "cidade": "Belo Horizonte"},
    {"nome": "Diego cirilo", "matricula": "202504", "idade": 21, "cidade": "Salvador"},
    {"nome": "Eduarda Lima", "matricula": "202505", "idade": 23, "cidade": "Curitiba"}
]
    context = {
        "usuarios": user_list, 
    }

    return render(request, 'usuario.html', context )
    