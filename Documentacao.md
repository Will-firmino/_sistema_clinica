# Django

# Comandos principais

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> venv\Scripts\activate
3. Instalar o django no projeto -> pip install django
4. Para criar um projeto Django -> django-admin startproject project .
5. Para subir o servidor -> python manage.py runserver
6. Parar criar um novo app -> python manage.py startapp sistema
7. Parar criar um superuser -> python manage.py createsuperuser
8. Para alterar a senha, caso você esqueça -> python manage.py changepassword nomedousuario

# PRINCIPAIS ARQUIVOS/PASTAS DO PROJECT
1. settings.py -> é o arquivo de configuração do projeto.
2. urls.py -> é o arquivo base [principal] de urls do projeto.


# DOCUMENTAÇÃO
1. `urls` -> https://docs.djangoproject.com/en/5.1/topics/http/urls/ 
2. `settings` -> https://docs.djangoproject.com/en/5.1/topics/settings/ , https://docs.djangoproject.com/en/5.1/ref/settings/



# Criação das entidades do sistema
[PACIENTE]
nome
sobrenome
email
telefone
criação
mensagem
ativo
imagem
