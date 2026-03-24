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

def OpenChrome():
    # ---------------------------------------- Step 1 - Acess interprise system ----------------------------
    # Initialize Chrome browser
    Browser = webdriver.Chrome()

    # Open a site using URL
    Browser.get("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")

    # Maxize window
    py.hotkey('win', 'up')

def Login():
    # ---------------------------------------- Step 2 - Login on system --------------------------------------
    # Login (User name)
    py.press('tab')
    py.write('Claudio_litz')
    time.sleep(1)

    # Login (Password)
    py.press('tab')
    py.write('senhaforte')
    time.sleep(1)

    # Enter to acess
    py.press(['tab','enter'])
    time.sleep(3)

def download():
    # ---------------------------------------- Step 3 - Download DB ----------------------------------------------
    py.click(1181,339)
    time.sleep(3)
    py.alert("Downloaded file? ")


def CalculateIndicators():
    # ---------------------------------------- Step 4 - Calculate indicators --------------------------------------
    # DB import
    table = pd.read_csv(r"C:\Users\claudio_litz\Downloads\Compras.csv", sep=';')
    print(table)


    total_spent = table["ValorFinal"].sum()
    quantity = table["Quantidade"].sum()
    avarage_price = table["ValorUnitário"].mean()

    print(total_spent)
    print(quantity)
    print(avarage_price)



def __init__():
    # Step 0 - Program start alert
    py.alert("Wait program finish to back")

    OpenChrome()            # Fuction that will open Chrome browser
    Login()                 # Fuction to login in enterprise system
    download()              # Function to download DB
    CalculateIndicators()   # Function to calculate an indicators

    input("Press enter to finish program...")































__init__()
