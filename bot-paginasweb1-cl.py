import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# configuración
NUM_NAVEGADORES = 3
URL = 'https://www.youtube.com/watch?v=BeLoTpLr96s'
TIEMPO_VISTA = 5

# crear la lista de navegadores
navegadores = []
for _ in range(NUM_NAVEGADORES):
    options = webdriver.ChromeOptions()
    #PROXY = "45.131.6.108:80" ACA PUEDES AGREGAR UN PROXY COMO EL EJEMPLO QUE ESTA 
    #options.add_argument('--proxy-server=%s' % PROXY) DESCOMENTAR ESTO SI VAS A UTILIZAR UN PROXY
    navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    navegador.get(URL)
    navegadores.append(navegador)

# función para actualizar un navegador
def actualizar_navegador(navegador):
    # esperar a que el contenido se cargue
    wait = WebDriverWait(navegador, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
    # actualizar la página
    navegador.refresh()

# ciclo principal
while True:
    # seleccionar un navegador aleatorio
    navegador_actual = random.choice(navegadores)
    # actualizar el navegador
    actualizar_navegador(navegador_actual)
    print(f"Navegador {navegadores.index(navegador_actual)} actualizado")
    # esperar un tiempo aleatorio antes de la próxima actualización
    time.sleep(random.uniform(TIEMPO_VISTA * 0.5, TIEMPO_VISTA * 1.5))
