import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

articulo = input("Seleccione el artículo a buscar: ")
cantidad = int(input("Seleccione la cantidad de artículos a buscar: "))

def busqueda(articulos, cantidades):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020, 1200")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A2811119011&language=es&ref=nav_em__nav_desktop_sa_intl_cell_phones_and_accessories_0_2_5_5")
    time.sleep(5)

    txtemail = navegador.find_element(By.ID, "twotabsearchtextbox")
    txtemail.send_keys(articulos)
    time.sleep(5)

    txtlogin = navegador.find_element(By.ID, "nav-search-submit-button")
    txtlogin.click()

    time.sleep(5)
    data = {"Nombre": [], "Precio": [], "Envio": [], "Estrellas": []}

    while cantidades > 0:
        tarjetas = navegador.find_elements(By.CLASS_NAME, "a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small")

        for tarjeta in tarjetas:
            nombres = tarjeta.find_elements(By.TAG_NAME, "h2")

            if nombres:
                nombre = nombres[0].text
                data["Nombre"].append(nombre)
            else:
                data["Nombre"].append("None")

            precios = tarjeta.find_elements(By.CLASS_NAME, "a-price")
            if precios:
                precio = precios[0].text
                data["Precio"].append(f"${precio}")
            else:
                data["Precio"].append("None")

            entregas = tarjeta.find_elements(By.CLASS_NAME, "a-color-base.a-text-bold")
            if entregas:
                entrega = entregas[0].text
                data["Envio"].append(entrega)
            else:
                data["Envio"].append("None")

            ratings = tarjeta.find_elements(By.XPATH, ".//span[@aria-label]")
            if ratings:
                rating = ratings[0].text
                data["Estrellas"].append(rating)
            else:
                data["Estrellas"].append("None")

            cantidades -= 1

            if cantidades == 0:
                break

        print(f"Quedan {cantidades} artículos por buscar, pasando a la siguiente página")
        siguiente_pagina = navegador.find_elements(By.CLASS_NAME, "s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")

        if siguiente_pagina:
            siguiente_pagina[0].click()
            time.sleep(2)
        else:
            print("No hay más páginas disponibles.")
            break

    archivo = pd.DataFrame(data)
    archivo.to_csv("Amazon_Puma.csv", index=False)

busqueda(articulo, cantidad)