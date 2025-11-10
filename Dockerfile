# Utilise une image python
FROM python:3.11-slim

# Def le dossier de travail 
WORKDIR /app

# Copier les fichiers présents
COPY . .

# Installer les libraries
RUN pip install -r requirements.txt

# Exec le main 
CMD ["python","src/main.py"]