from setuptools import setup, find_packages

setup(
    name="testrepo",                           # Nombre del paquete
    version="0.1.0",                                # Versión inicial
    packages=find_packages(),                       # Paquetes a incluir
    description="Un paquete pip simple de saludo",  # Breve descripción
    author="A gavilan",                         # Tu nombre
    author_email="gavilan@gmail.com",                 # Tu correo electrónico
    url="https://github.com/Andresgavilan/testrepo",     # URL del proyecto
)