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
# Encontrar a div inicial
div_inicial = nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div')
# nav.find_element('xpath','//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[2]').click()
# sleep(1)
nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[2]/div[3]').click()
sleep(1)

nomes = []
for c in range(0,2):
    for x in range(10,0,-1):
        print(x)
        nomes.append(nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[{x}]/div[3]/div/span').text)
    nav.find_element('xpath','//*[@id="app"]/div/div[4]/div[2]/div[2]/div[1]').click()
    sleep(1)
print(nomes)

dftest = pd.DataFrame()

colunas = ['primeiro','segundo','terceiro','quarto','quinto','sexto','sétimo','oitavo','nono','decimo','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte','final']
for c in range(0,len(nomes)):
    if nomes[c] == 'Grande':
        valor = 1
    else:
        valor = 0
    dftest[colunas[c]] = [valor]

previ = tr.predict(dftest)
vp = None
taxa = None
if previ < 0.5:
    vp = 'Pequeno'
    if previ > 0 or previ == 0:
        taxa = 100 - (previ * 100)
    elif previ >-1:
        taxa =  previ*-100
    else:
        taxa = 0
else:
    vp = 'Grande'
    if (previ > 1  and previ < 2) or previ == 1:
        taxa = 100 - ((previ-1) * 100)
    elif previ < 1:
        taxa = previ * 100
    else:
        taxa = 0

if taxa > 74.99:
    n_jogos = 1
else:
    n_jogos = 0

print(f'Previsão: {vp}\n Chance de acerto: {taxa} \n Valor: {previ}')

jogada = nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div').text
acertos = 0
taxa_acertos = 0
nova_jogada = nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div').text
while True:
    count2 = 0
    while jogada == nova_jogada:
        print(jogada)
        print(nova_jogada)
        sleep(5)
        if count >= 10:
            nav.get('https://popbra.com/#/win')
        try:
            nova_jogada = nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div').text
        except:
            sleep(2)
            nova_jogada = nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div').text
        count2 += 1
    jogada = nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div').text
    valor = nav.find_element('xpath',f'//*[@id="app"]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/span').text
    if valor == vp and taxa > 74.99:
        acertos += 1
    if taxa > 74.99:
        taxa_acertos = (acertos*100)/n_jogos
    print(f'######TAXA DE ACERTOS DE: {taxa_acertos} >>>> {n_jogos}#################')
    if valor == 'Grande':
        dftest['final'] = [1]
    else:
        dftest['final'] = [0]
    df = pd.concat([df,dftest])
    df.to_csv('projeto_brincante/hehe4.csv',index=False)
    y = df['final']
    x = df.loc[:,df.columns != 'final']
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)
    tr.fit(x_train,y_train)
    print(dftest)
    for c in range(0,len(dftest.columns)-1):
        dftest[colunas[c]] = dftest[colunas[c+1]]
    print(dftest)
    previ = tr.predict(dftest.drop('final',axis=1))
    vp = None
    taxa = None
    if previ < 0.5 :
        vp = 'Pequeno'
        if previ > 0 or previ == 0:
            taxa = 100 - (previ * 100)
        elif previ >-1:
            taxa =  previ*-100
        else:
            taxa = 0
    else:
        vp = 'Grande'
        if (previ > 1  and previ < 2) or previ == 1:
            taxa = 100 - ((previ-1) * 100)
        elif previ < 1:
            taxa = previ * 100
        else:
            taxa = 0

    if taxa > 74.99:
        n_jogos += 1
  

    print(f'Previsão: {vp}\n Chance de acerto: {taxa} \n Valor: {previ}')
    nav.get('https://popbra.com/#/win')


# Encontrar todas as divs dentro da div inicial
input('xx')
divs = div_inicial.find_element('xpath','.//div')
print(divs)
# Iterar sobre as divs e obter o texto
for div in divs:
    # Encontrar as três divs dentro de cada div
    divs_internas = div.find_element('xpath','.//div')

    # Verificar se existem exatamente três divs internas
    if len(divs_internas) == 3:
        # Extrair o texto das três divs internas
        texto_div1 = divs_internas[0].text
        texto_div2 = divs_internas[1].text
        texto_div3 = divs_internas[2].text

        # Fazer o que for necessário com o texto das divs
        print(texto_div1)
        print(texto_div2)
        print(texto_div3)


    


        


