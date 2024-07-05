import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Ruta del archivo Excel que contiene las cédulas a buscar
ruta_excel = r'C:\Users\admin\Documents\GitHub\Busqueda-RUT-automatica\Cedulas.xlsx'
# Leer solo la columna A
df = pd.read_excel(ruta_excel, usecols="A")  

# Convertir la columna de cédulas a una lista
cedulas = df.iloc[:, 0].tolist()

# Configurar Selenium y abrir el navegador en la página de la Dian
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces')

def buscar_cedula(cedula):
    try:
        # Esperar hasta 5 segundos para que el elemento del campo de texto esté presente
        input_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit'))
        )
        input_element.clear()
        input_element.send_keys(cedula)
        input_element.send_keys(Keys.RETURN)

        # Esperar hasta 1 segundos para que aparezca el pop-up de error de búsqueda o los resultados
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.elDivScroll'))
            )
            # Si llegamos aquí, significa que se encontró el pop-up de error y que la cédula no tiene RUT
            return False
        except TimeoutException:
            # Si no se encuentra el pop-up de error, asumimos que la cédula SÍ tiene RUT
            return True

    except Exception as e:
        print(f"Error al buscar cédula {cedula}: {str(e)}")
        return False

# Archivo de texto para guardar los resultados
with open('resultados.txt', 'w') as file:
    for cedula in cedulas:
        if buscar_cedula(cedula):
            #Escribe la cédula y un " - 1 " si la cédula tiene RUT
            file.write(f'{cedula} - 1\n')
        else:
            #Escribe la cédula y un " - 0 " si la cédula NO tiene RUT
            file.write(f'{cedula} - 0\n')

# Cerrar el navegador
driver.quit()