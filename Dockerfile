# Dockerfile para Django + Poetry (Python 3.10)

FROM python:3.10-slim

# Instala dependências de sistema
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do Poetry para instalar dependências
COPY poetry.lock pyproject.toml /app/

# Instala Poetry
RUN pip install poetry

# Instala as dependências do projeto (exceto o próprio projeto)
RUN poetry install --no-root --no-interaction

# Copia todo o código-fonte para a imagem
COPY . /app/

# Coleta arquivos estáticos (o comando NÃO irá falhar se não existir static/ ainda)
RUN poetry run python manage.py collectstatic --noinput

# Expõe a porta utilizada pelo Gunicorn
EXPOSE 8000

# Comando para iniciar o servidor (ajuste conforme o nome do seu módulo wsgi, padrão: marmitex)
CMD ["poetry", "run", "gunicorn", "marmitex.wsgi:application", "--bind", "0.0.0.0:8000"]
