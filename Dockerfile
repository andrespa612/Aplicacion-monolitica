# Dockerfile

# Usamos una imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos de la aplicación al contenedor
COPY . .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 5000 para que la aplicación Flask pueda ser accesible
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "app.py"]
