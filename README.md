
Script em python recebe um arquivo csv contendo uma lista de aspectos, e devolve agrupamentos de aspectos com mesmo significado, ou significados muito semelhantes.
A saída do algoritmo, com os respectivos grupos formados encontra-se no arquivo 'saida.txt'

## Uso

Este projeto requer a utilização de Python 3, e da biblioteca NLTK. <br>
[Instale e configure o Python 3](https://www.python.org/downloads/)

Instale as dependências <br>
`pip install -r requirements.txt`

Rode o programa <br>
`python agrupamento.py`

## Bibliotecas
### Wordnet
O WordNet é um leitor de corpus da biblioteca NLTK que possui um banco de dados lexical de inglês. <br>
Substantivos, verbos, adjetivos e advérbios são agrupados em conjuntos de sinônimos cognitivos (synsets), cada um expressando um conceito distinto. Os synsets são interligados por meio de relações conceitual-semânticas e lexicais. <br>
Foram utilizados neste projeto seus métodos para encontrar os synsets e a o método wup_similarity, que calcula o grau de similaridade de duas palavras, variando de 0 à 1.
