# 🔍 Consultor de CEP - Django

Este é um projeto Django que permite aos usuários **se cadastrar, fazer login e consultar endereços via CEP** utilizando a API do ViaCEP.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Django 5.x**
- **Bootstrap 5 (para estilização)**
- **API ViaCEP (para consulta de endereços)**

---

## 📌 Requisitos para Executar o Projeto

Antes de rodar o projeto, certifique-se de ter o **Python 3** instalado. Se ainda não tem o **pipenv**, instale com:

```bash
pip install pipenv
```
###  Como Instalar e Rodar o Projeto
- Clone este repositório
```bash
git clone https://github.com/TN-Junior/search-cep-with-django.git
```
- Entre no diretório do projeto
```bash
cd search-cep-with-django
```
- Crie um ambiente virtual e ative-o
```bash
pipenv install
pipenv shell
```
- Instale as dependências do projeto
```bash
pip install -r requirements.txt
```
- Realize as migrações do banco de dados
```bash
python manage.py migrate
```
- Crie um superusuário (opcional para acessar o Django Admin)
```bash
python manage.py createsuperuser
```
- Inicie o servidor local
```bash
python manage.py runserver
```
- Acesse o sistema no navegador:
http://127.0.0.1:8000/

### *Como Criar Conta e Fazer Login*
**1 Registro de novo usuário**
- Acesse http://127.0.0.1:8000/register/
- Preencha os campos Usuário, Senha e Confirmação de Senha
- Clique em Registrar
- Você será autenticado automaticamente e redirecionado para a página inicial.
  
**2 Login**
- Acesse http://127.0.0.1:8000/login/
- Insira seu usuário e senha
- Clique em Entrar
- Após logar, você pode consultar CEPs.

**3 Logout**
- Clique no botão Sair na barra de navegação.

### Como Consultar um CEP
- Acesse a página principal: http://127.0.0.1:8000/
- Digite um CEP no campo de busca
- Clique em "Consultar"
- O endereço será exibido na tela com informações como rua, bairro, cidade e estado.



