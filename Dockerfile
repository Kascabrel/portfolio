FROM python:3.12-slim

WORKDIR /app

# Installer pip et dépendances pour builder
RUN pip install --upgrade pip setuptools wheel

# Copier requirements.txt
COPY requirements.txt /app/

# Installer toutes les dépendances via pip
RUN pip install -r requirements.txt

# Copier tout le code
COPY . /app

EXPOSE 5200

# Lancer l'app avec Gunicorn
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5200", "--workers", "4"]
