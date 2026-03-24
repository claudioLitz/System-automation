# Passo 1 - Acessar o sistema de empresa
# Passo 2 - Fazer login nos sistemas
# Passo 3 - Baixar a base de dados
# Passo 4 - Calcular os indicadores
# passo 5 - Enviar o e-mail tratado para outro setor ou diretoria


import pyautogui as py
from selenium import webdriver 
import pyperclip
import time
import pandas as pd

# Step 0 - Program start alert
py.alert("Espere o programa terminar para voltar a mexer")


# ---------------------------------------- Step 1 - Acess interprise system ----------------------------
# Initialize Chrome browser
navegador = webdriver.Chrome()

# Open a site using URL
navegador.get("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")

# Maxize window
py.hotkey('win', 'up')

# ---------------------------------------- Passo 2 - Fazer login nos sistemas --------------------------------------
# Login (User name)
py.press('tab')
py.write('Claudio_litz')
time.sleep(1)

# Login (Password)
py.press('tab')
py.write('senhaforte')
time.sleep(1)

# Pressionar Enter
py.press(['tab','enter'])
time.sleep(3)

# ---------------------------------------- Passo 3 - Baixar a base de dados ----------------------------------------------
py.click(1181,339)
time.sleep(1)
py.alert("Arquivo baixado? ")

# ---------------------------------------- Passo 4 - Calcular os indicadores
# Importe da base de dados
tabela = pd.read_csv(r"C:\Users\claudio_litz\Downloads\Compras.csv", sep=';')
print(tabela)



input("Pressione Enter para fechar o navegador...")