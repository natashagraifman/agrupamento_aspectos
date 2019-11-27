import nltk
import csv
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

aspectos = []

#lendo os aspectos do arquivo csv e colocando-os na lista aspectos
with open('laptop_filtered_aspect_sample.csv') as ficheiro:
    leitor = csv.reader(ficheiro)
    aspectos = [linha[0] for linha in leitor]

# função que recebe como entrada duas strings e retorna verdadeiro se as duas são sinonimos (de acordo com a classificação de synsets do wordnet), ou se possuem similaridade acima de 90%)
def similares(s1,s2):
    resultado = False
    for syn1 in wn.synsets(s1):
        for syn2 in wn.synsets(s2):
            if (wn.wup_similarity(syn1,syn2) is not None):
                if (wn.wup_similarity(syn1,syn2)>=0.9):
                    resultado = True
                    return resultado
    return resultado

# função que escreve no arquivo
def adiciona_arquivo(sinonimos):
    string_sinonimos = ' '.join([str(item) for item in sinonimos])

    arquivo = open('saida.txt', 'r') # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append('\n Grupo: ')
    conteudo.append(string_sinonimos)   # insira seu conteúdo

    arquivo = open('saida.txt', 'w') # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)   # escreva o conteúdo criado anteriormente nele.

    arquivo.close()

# função que recebe como entrada uma lista de strings, e agrupa os aspectos que são semelhantes, retornando todos os grupos da lista
def agrupamento(lista):
    if lista:
        for item in lista:
            sinonimos=[]
            for comparando in lista:
                if(comparando in sinonimos):
                    lista.remove(comparando)
                elif (similares(item, comparando)):
                    sinonimos.append(comparando)
                    lista.remove(comparando)
            if(sinonimos):
                adiciona_arquivo(sinonimos)
                print(sinonimos)

agrupamento(aspectos)
