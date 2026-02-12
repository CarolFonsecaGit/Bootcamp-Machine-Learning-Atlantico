# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def impares(numeros):
    impares = []
    for num in numeros:
        if num % 2 != 0:
            impares.append(num)
    return impares

impares_lista = impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Q1 - ", impares_lista)

# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
def primos(numeros):
    primos = []
    for num in numeros:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos

primos_lista = primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13])
print("Q2 - ", primos_lista)

# 3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def diferenca(lista1, lista2):
    diferenca = []
    for item in lista1:
        if item not in lista2:
            diferenca.append(item)
    for item in lista2:
        if item not in lista1:
            diferenca.append(item)
    return diferenca

diferenca_lista = diferenca([1, 2, 3, 4], [3, 4, 5, 6])
print("Q3 - ", diferenca_lista)

# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
def segundo_maior(numeros):
    maior = max(numeros)
    numeros.remove(maior)
    return max(numeros)

segundo_maior_valor = segundo_maior([5, 2, 4, 3, 6, 12])
print("Q4 - ", segundo_maior_valor)

# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda x: x[0])

pessoas = [("Carol", 20), ("Teodoro", 4), ("Clara", 25), ("Ana", 30)]
pessoas_ordenadas = ordenar_por_nome(pessoas)
print("Q5 - ", pessoas_ordenadas)

# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?
import statistics

def identificar_outliers(numeros):
    media = statistics.mean(numeros)
    desvio_padrao = statistics.stdev(numeros)
    limite_inferior = media - 2 * desvio_padrao
    limite_superior = media + 2 * desvio_padrao
    outliers = [x for x in numeros if x < limite_inferior or x > limite_superior]
    return outliers

numeros = [10, 12, 12, 13, 12, 11, 14, 100]
outliers = identificar_outliers(numeros)
print("Q6 - ", outliers)

# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})
df_concatenado = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Q7 - ", df_concatenado)

# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
"""
df = pd.read_csv('arquivo.csv')
print("Q8 - ", df.head())
"""
print("Q8 - Comentada no script")

#9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
df = pd.DataFrame({'Nome': ['Carol', 'Teodoro', 'Clara'], 'Idade': [20, 4, 25]})
filtro_idade = df[df['Idade'] > 18]
print("Q9 - ", filtro_idade)

# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
"""
Q10 - No pandas, lidar com valores ausentes é algo bem
comum no dia a dia de análise de dados. Primeiro, você pode
identificar onde existem valores faltando usando isna() ou isnull(), que mostram
quais posições estão com NaN. Se a quantidade de valores ausentes
for pequena, uma opção simples é removê-los com dropna(). Mas muitas
vezes não é interessante apagar dados, então você pode preencher
esses valores com fillna(). Dá para substituir por um valor fixo
(como 0), pela média ou mediana da coluna, ou até usar métodos como 
fill, que preenche com o valor anterior — algo muito útil em séries
temporais. No fim, a melhor escolha depende do tipo de dado e do objetivo
da análise.
"""
print("Q10 - Comentada no script")