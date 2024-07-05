# Busqueda RUT automatica
¡Hola, soy Steban y te doy la bienvenida a este repositorio!

Este script permite automatizar la búsqueda de cédulas en la página de consulta de estado RUT de la DIAN y genera un archivo de texto con los resultados, indicando si cada cédula tiene RUT o no.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Requisitos**
1. Python


2. Dependencias: Instala las bibliotecas necesarias utilizando pip. Abre una terminal y ejecuta los siguientes comandos:

pip install pandas

pip install selenium

pip installwebdriver-manager

pip installopenpyxl



3. Archivo Excel: Debes tener un archivo Excel que contenga las cédulas en la columna A. La ruta de este archivo debe ser especificada en la variable ruta_excel dentro del script.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Instrucciones**

1. Configuración del Script:

Abre el archivo busqueda_rut.py en un editor de texto o IDE.

Cambia la variable ruta_excel para que apunte a la ubicación de tu archivo Excel. Por ejemplo:

ruta_excel = r'C:\Users\admin\Documents\GitHub\Busqueda-RUT-automatica\Cedulas.xlsx'

2. Ejecución del Script:

Abre una terminal o línea de comandos.

Navega hasta el directorio donde guardaste el archivo busqueda_rut.py.

Ejecuta el script con UNO de los siguientes comandos:

python busqueda_rut.py

py busqueda_rut.py

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Resultados**

El script abrirá una ventana de Google Chrome y comenzará a buscar cada cédula en la página de la DIAN.
Los resultados se guardarán en un archivo llamado resultados.txt en el mismo directorio donde se encuentra el script.
En resultados.txt, cada línea tendrá el formato cédula - X, donde X será 1 si la cédula tiene RUT y 0 si no tiene RUT.
Detalles del Código.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**¿Cómo funciona el código?**

Importación de Bibliotecas: El script utiliza pandas para leer el archivo Excel, selenium para automatizar el navegador, y webdriver-manager para gestionar la descarga de ChromeDriver.

Configuración del Navegador: Utiliza webdriver.Chrome para abrir una instancia de Google Chrome y navegar a la página de consulta de estado RUT de la DIAN.

Función buscar_cedula: Esta función toma una cédula como entrada, la busca en la página de la DIAN y devuelve True si la cédula tiene RUT y False si no la tiene.

Archivo de Resultados: El script escribe los resultados en resultados.txt, indicando si cada cédula tiene RUT (1) o no (0).

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Siéntete libre de usar y modificar el código para adaptarlo a tus necesidades. :)

Si tienes algún problema, pregunta o sugerencia, no dudes en contactarme vía Discord: SkilleD#2857
