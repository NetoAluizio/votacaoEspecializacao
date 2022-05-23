#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Análise de votação para curso de especialização:

# Opções e votação(respostas)

engenhariaSoftware = 0
pythonDataScience = 1
introducaoJava = 2
respostas = [
    1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
  1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
  2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1
]

# Separação por votos

escolhaEngenharia = respostas.count(0)
escolhaDataScience = respostas.count(1)
escolhaJava = respostas.count(2)

# Ordenação e organização dos votos

escolhas = [escolhaEngenharia, escolhaDataScience, escolhaJava]
vencedora = sorted(escolhas)
totalVotos = len(respostas)

# Votos em percentuais

percentualEngenharia = (escolhaEngenharia/totalVotos)*100
percentualDataScience = (escolhaDataScience/totalVotos)*100
percentualJava = (escolhaJava/totalVotos)*100

print('Ao todo foram', totalVotos, 'votos.')
print(escolhaEngenharia, 'para Engenharia de Software; representando', percentualEngenharia, '% dos votos.')
print(escolhaDataScience, 'para Data Sciense; representando', percentualDataScience, '% dos votos.')
print(escolhaJava, 'para Java; representando', percentualJava, '% dos votos.')
if(percentualEngenharia > percentualDataScience and percentualEngenharia > percentualJava):
    print('O vencedor foi o curso de Engenharia de Software!')
elif(percentualDataScience > percentualEngenharia and percentualDataScience > percentualJava):
    print('O vencedor foi o curso de Python para Data Science!')
else:
    print('O vencedor foi o curso de Introdução ao Java!')

