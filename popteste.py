# from sklearn.tree import DecisionTreeClassifier
# import numpy as np

# # Define o número de entradas para cada amostra
# n_inputs = 20

# # Inicializa o histórico com uma sequência aleatória de 0's e 1's
# history = list(np.random.randint(0, 2, size=n_inputs))

# # Inicializa o modelo de Árvore de Decisão
# clf = DecisionTreeClassifier()

# while True:
#     if len(history) > n_inputs:
#         # Gera um conjunto de treinamento com as últimas n_inputs amostras
#         X_train = np.array(history[-n_inputs-1:-1]).reshape(1, -1)
#         y_train = np.array(history[-1]).reshape(1, )
        
#         # Treina o modelo com o conjunto de treinamento atual
#         clf = clf.fit(X_train, y_train)
    
#     if len(history) == n_inputs:
#         # Faz a previsão para a próxima entrada com base no histórico atual
#         next_guess = clf.predict(np.array(history[-n_inputs:]).reshape(1, -1))[0]
#     else:
#         # Se ainda não houver histórico suficiente para prever, chuta aleatoriamente
#         next_guess = np.random.randint(0, 2)
        
#     # Lê as entradas atuais
#     current_inputs = int(input("Digite a entrada (0 ou 1): "))
    
#     # Adiciona as entradas ao histórico
#     history.append(current_inputs)

#     if current_inputs == next_guess:
#         print("Acertou!")
#     else:
#         print("Errou!")
        
#         # Adiciona as entradas incorretas ao histórico de treinamento
#         X_train = np.array(history[-n_inputs-1:-1]).reshape(1, -1)
#         y_train = np.array(current_inputs).reshape(1, )
        
#         # Treina o modelo com o conjunto de treinamento atualizado
#         clf = clf.fit(X_train, y_train)
    
#     # Calcula a porcentagem de acertos
#     correct_guesses = sum(1 for i in range(n_inputs) if history[-n_inputs+i] == history[-n_inputs+i+1])
#     accuracy = correct_guesses / n_inputs * 100
#     print(f"Porcentagem de acerto: {accuracy:.2f}%")

from time import sleep
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# # Define o número de elementos na sequência
n_inputs = 20

# # Inicializa a sequência com uma lista aleatória de 0's e 1's
sequence = list(np.random.randint(0, 2, size=n_inputs))

# for c in range(0,20):
#     sequence.append(int(input(': ')))
# Inicializa o modelo de Árvore de Decisão
clf = DecisionTreeClassifier()

# Define a variável para contar o número de acertos
num_correct = 0
 # Gera um conjunto de treinamento com as últimas n_inputs amostras
X_train = np.array(sequence[-n_inputs:]).reshape(1, -1)
count = 0
while True:
    if count == 1000:
        sleep(1)
        count=0
   

    # Pede ao usuário para informar o próximo elemento da sequência
    next_element = np.random.randint(0,2)
    print(next_element)
    

    # Faz a previsão para o próximo elemento com base no histórico atual
    try:
        next_guess = clf.predict(X_train)[0]
    except:
        print('quem quem quem')
        next_guess = 0

    if next_element == next_guess:
        print("Acertou!"+str(n_inputs))
        print(sequence[-n_inputs:])
        num_correct += 1
    else:
        print("Errou!")
        num_correct = 0
        n_inputs += 1
        # Adiciona o elemento incorreto à sequência
        sequence.append(next_element)

        # Atualiza o conjunto de treinamento
        X_train = np.array(sequence[-n_inputs:]).reshape(1, -1)
        y_train = np.array(sequence[-1]).reshape(1, )

        # Treina o modelo com o conjunto de treinamento atualizado
        clf = clf.fit(X_train, y_train)

    # Calcula e imprime a porcentagem de acertos
    accuracy = num_correct / (num_correct + 1)
    print("Porcentagem de acertos: {:.2f}%\n".format(accuracy * 100))
    count+=1

