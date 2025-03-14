from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')  # Redireciona usuários não autenticados para a página de login
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')  
def consulta_api(request):
    url = 'https://viacep.com.br/ws/'
    formato = '/json/'
    context = {}

    if 'buscar' in request.GET:
        cep = request.GET['buscar'].replace('-', '').strip()

        if len(cep) == 8 and cep.isdigit():
            try:
                response = requests.get(url + cep + formato)
                response.raise_for_status()
                data = response.json()

                context = {
                    'key_cep': data.get('cep', 'Não encontrado'),
                    'key_rua': data.get('logradouro', 'Não encontrado'),
                    'key_complemento': data.get('complemento', 'Não encontrado'),
                    'key_bairro': data.get('bairro', 'Não encontrado'),
                    'key_localidade': data.get('localidade', 'Não encontrado'),
                    'key_uf': data.get('uf', 'Não encontrado'),
                    'key_ddd': data.get('ddd', 'Não encontrado'),
                }
            except requests.exceptions.RequestException:
                context = {'result': 'Erro ao consultar o CEP. Tente novamente.'}
        else:
            context = {'result': 'CEP inválido! Digite um CEP válido com 8 números.'}
    else:
        context = {'result': 'O CEP NÃO FOI INFORMADO!'}

    return render(request, 'resultado.html', context)
