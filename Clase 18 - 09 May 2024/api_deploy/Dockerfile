# Image
FROM python:3.10-slim

# Wordir
WORKDIR /app

# Copiar requirements
# python -m pip freeze > requirements.txt
COPY requirements.txt .

# Librerias
#RUN pip install --no-cache-dir fastapi uvicorn pandas statsmodels
RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la app
COPY . .

# Exponer puerto donde la app corre 
EXPOSE 8000

# Correr la app 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t david_app .
# docker run -d -p 8000:8000 david_app

