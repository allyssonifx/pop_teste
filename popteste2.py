from time import sleep
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico, options=chrome_options)
nav.get('https://popbra.com')
sleep(10)
print('indo')
nav.get('https://popbra.com/#/home')
sleep(5)
nav.find_element('xpath','/html/body/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]').click()
sleep(3)
nav.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/input').send_keys('xxxx')
nav.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[3]/input').send_keys('xxxx')
nav.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[4]/button').click()
sleep(3)
nav.find_element('xpath','/html/body/div[3]/div[3]/button').click()
nav.find_element('xpath','/html/body/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]').click()
sleep(5)
item = 'Pequeno'
teste = ''
count = 0
acertos = 0
erros = 0
rodadas = 11
vez = int(input('x'))
while True:
    tempo = time.time()
    nav.get('https://popbra.com/#/win')
    sleep(3)
    nome = nav.find_element('xpath','/html/body/div[1]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/span').text
    print(nome)
    print(vez)
    vez += 1
    count += 1
    if nome == teste:
        acertos += 1
        teste = ''
        count = 1
    elif count > rodadas:
        erros += 1
        teste = ''
        count = 0
    else:
        if nome == item:
            if count == rodadas and str(nome) == 'Pequeno':
                teste = 'Grande'
                print('>>>>Vai dar Grande<<<')
            elif count == rodadas and str(nome) == 'Grande':
                teste = 'Pequeno'
                print('>>>>Vai dar Pequeno<<<')
        else:
            item = nome
            count = 1

            print('o item agora é>>'+str(nome))
    print('ACERTOS: '+str(acertos))
    print('ERROS: '+str(erros))
    print('COUNT: '+str(count))
    tempoagr = str(time.time() - tempo).split('.')
    print(tempoagr)
    tempoagr = int(tempoagr[0])
    print(tempoagr)
    reloginho = 60 - tempoagr
    sleep(reloginho)
    


        


