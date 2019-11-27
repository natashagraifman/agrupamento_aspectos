
import nltk
import csv
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn

aspectos = []

#lendo os aspectos do arquivo csv e colocando-os na lista aspectos
with open('laptop_filtered_aspect_sample.csv') as ficheiro:
    leitor = csv.reader(ficheiro)
    aspectos = [linha[0] for linha in leitor]

lista = ['computer','laptop','price','calculator','screen','display','cost','estimator','dog','notebook']

# função que recebe como entrada duas strings e retorna verdadeiro se as duas são sinonimos (de acordo com a classificação de lemmas do wordnet), ou se possuem similaridade acima de 90%)
def similares(s1,s2):
    resultado = False
    for syn1 in wn.synsets(s1):
        for syn2 in wn.synsets(s2):
            if (wn.wup_similarity(syn1,syn2) is not None):
                if (wn.wup_similarity(syn1,syn2)>=0.9):
                    resultado = True
                    return resultado
    return resultado

# função que recebe como entrada uma lista de strings, e agrupa os aspectos que são semelhantes, retornando todos os grupos da lista
def agrupamento(lista):
    grupos=[]
    if lista:
        for item in lista:
            sinonimos=[]
            for comparando in lista:
                if(comparando in sinonimos):
                    lista.remove(comparando)
                elif (similares(item, comparando)):
                    sinonimos.append(comparando)
                    lista.remove(comparando)
            if (sinonimos not in grupos):
                grupos.append(sinonimos)
                print(sinonimos)
                print(len(lista))
    return grupos
'''
for syn in wn.synsets("needs"):
    print(syn, syn.definition())
    #for l in syn.lemmas():
        #print(syn)
'''

for syn in wn.synsets('dog'):
    for l in syn.lemmas():
        print(l.name())

def similaridade(s1,s2):
    for syn1 in wn.synsets(s1):
        for syn2 in wn.synsets(s2):
            print(syn1, syn1.definition())
            print(syn2, syn2.definition())
            print(wn.wup_similarity(syn1,syn2))

#similaridade('computer','clients')

#print(similares('laptop','notebook'))
#print(agrupamento(aspectos))
