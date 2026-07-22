from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Edge()
driver.get("https://resultado.chiptiming.com.br/resultados/2025/100saosilvestre")
time.sleep(6)
cards = driver.find_elements(By.CLASS_NAME, "resultado-card")

print("Total de cards encontrado:", len(cards))
print(driver.page_source[:5000])

for c in cards[:10]:
    print(c.text)

driver.quit()
