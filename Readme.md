# requisitos
- python 3.8
- pip 20.0.2
- Postgresql 

# Instalação e ativação do projeto

### 1. clone o repositório na sua máquina:
```https://github.com/Me-Adota/website.git``` 

### 2. Ativar seu ambiente virtual:
```virtualenv {virtual_env_name}```

```source {virtual_env_name}/bin/activate```

### 3. Instalar os requerimentos do projeto
``` pip3 install -r requirements.txt```

### 4. Fazer todas as migrations do projeto
``` python3 manage.py makemigrations```

``` python3 manage.py migrate```

### 5. Rodar o servidor
``` python manage.py runserver```

A aplicação deverá estar rodando em sua máquina.


