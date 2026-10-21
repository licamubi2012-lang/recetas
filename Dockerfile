# Usamos la imagen oficial de SWI-Prolog como base para tener el motor real
FROM swipl:latest

# Actualizamos el sistema e instalamos Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Creamos una carpeta de trabajo dentro del servidor
WORKDIR /app

# Copiamos e instalamos las dependencias de Python (Flask) permitiendo la instalación global en el contenedor
COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Copiamos todo el código del proyecto (app.py, recetas.pl, carpeta templates, etc.)
COPY . .

# Abrimos el puerto 5000 para que la web pueda comunicarse
EXPOSE 5000

# Comando para encender la aplicación web al iniciar el servidor
CMD ["python3", "app.py"]