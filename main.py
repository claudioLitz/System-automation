import pyautogui as py
from selenium import webdriver
import time
import pandas as pd
from dotenv import load_dotenv
import os
import pyperclip

class AutomationBot:
    
    CSV_PATH = r"C:\Users\claudio_litz\Downloads\Compras.csv"

    def __init__(self):
        load_dotenv()
        self.browser = None
        self.table = None
        self.email = os.getenv("user_email")
        self.password = os.getenv("user_password")
        self.total_spent = None
        self.quantity = None
        self.average_price = None

    def open_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")

        self.browser = webdriver.Chrome(options=options)
        self.browser.get("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
        py.hotkey('win', 'up')
        time.sleep(2)

    def login(self, username: str, password: str):
        py.press('tab')
        py.write(username)
        time.sleep(1)

        py.press('tab')
        py.write(password)
        time.sleep(1)

        py.press(['tab', 'enter'])
        time.sleep(3)

    def download(self):
        time.sleep(3)
        py.click(1181, 339)
        time.sleep(6)
        py.press('enter')
        time.sleep(4)

    def load_data(self):
        self.table = pd.read_csv(self.CSV_PATH, sep=';')
        print(self.table)

    def calculate_indicators(self):
        if self.table is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        self.total_spent   = self.table["ValorFinal"].sum()
        self.quantity      = self.table["Quantidade"].sum()
        self.average_price = self.table["ValorUnitário"].mean()

        print(f"Total Spent:   {self.total_spent}")
        print(f"Quantity:      {self.quantity}")
        print(f"Average Price: {self.average_price}")

    def SendEmail(self):
        py.PAUSE = 0.5
        py.hotkey('ctrl', 't')
        py.write("gmail.com")
        py.press('enter')
        time.sleep(3)

        # Click "Sign in" button
        py.click(1101, 175)
        time.sleep(3)

        # Enter email and password
        py.write(self.email)
        py.press('enter')
        time.sleep(7)
        py.write(self.password)
        py.press('enter')
        time.sleep(15)

        # Write an email       
        py.press('c')
        time.sleep(3)
        py.write("henrique_schorck@estudante.sesisenai.org.br")
        py.press(['tab' for _ in range(2)])
        py.write("Cool subject")
        py.press('tab')
        email_body = f'''
                Prezado(a) henrique schorck, tudo bem? 
                Segue relatório completo sobre os dados de compras.
                Total de gastos: R$ {self.total_spent}
                Quantidade itens no total: {self.quantity}
                Tiket médio: R$ {self.average_price}

                Fico a disposição.
                Respeitosamente, Claudio Litz'''
        
        pyperclip.copy(email_body)
        py.hotkey('ctrl','v')
        py.press(['tab'])

    def run(self):
        py.alert("Wait for the program to finish before returning.")

        self.open_chrome()
        self.login(username='Claudio_litz', password='senhaforte')
        self.download()
        self.load_data()
        self.calculate_indicators()
        self.SendEmail()

        input("Press enter to finish program...")


bot = AutomationBot()
bot.run()
