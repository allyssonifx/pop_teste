from time import sleep
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


df =  pd.read_csv('projeto_brincante\hehe4.csv')
print(df.columns)
#df.drop('x',axis=1,inplace=True)
y = df['final']
x = df.loc[:,df.columns != 'final']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)


# rfr = RandomForestRegressor()
# rfr.fit(x_train,y_train)
tr = DecisionTreeRegressor()
tr.fit(x_train,y_train)
 
# lr = LinearRegression()

# lr.fit(x_train,y_train)

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
nav.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/input').send_keys('xxxxx')
nav.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[3]/input').send_keys('xxxxx')
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
# Encontrar a div inicial
div_inicial = nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div')
# nav.find_element('xpath','//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[2]').click()
# sleep(1)
nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[2]/div[3]').click()
sleep(1)

nomes = []
for c in range(0,3133):
    nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[2]/div[3]').click()
    # for x in range(10,0,-1):
    #     print(x)
    #     nomes.append(nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[{x}]/div[3]/div/span').text)
    # nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[2]/div[1]').click()
    #sleep(1)
print(nomes)

dftest = pd.DataFrame()

colunas = ['primeiro','segundo','terceiro','quarto','quinto','sexto','sétimo','oitavo','nono','decimo','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte','final']
for c in range(0,len(nomes)):
    if nomes[c] == 'Grande':
        valor = 1
    else:
        valor = 0
    dftest[colunas[c]] = [valor]


input('xx')