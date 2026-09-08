import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/tag/life/"

response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

citas = soup.find_all("div", class_="quote")

datos = []

for cita in citas:

    texto_cita = cita.find("span", class_="text").get_text(strip=True)

    autor = cita.find("small", class_="author").get_text(strip=True)

    etiquetas = [
        tag.get_text(strip=True)
        for tag in cita.find_all("a", class_="tag")
    ]

    datos.append({
        "cita": texto_cita,
        "autor": autor,
        "etiquetas": ", ".join(etiquetas)
    })

df = pd.DataFrame(datos)

df.to_csv("mensajes_vida.csv", index=False, encoding="utf-8-sig")

print(f"Se extrajeron {len(df)} citas.")
print("Archivo mensajes_vida.csv creado correctamente.")

