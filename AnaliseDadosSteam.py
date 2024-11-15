import csv
from collections import Counter

class AnaliseSteam:
    """Classe para análise de dados de jogos do Steam a partir de um arquivo CSV."""

    def __init__(self, arquivo):
        """
        Inicializa a classe com o caminho do arquivo CSV.
        
        Args:
            arquivo (str): Caminho para o arquivo CSV a ser analisado.
        """
        self.nome_arquivo = arquivo

    def calcular_percentual_tipos(self):
        """
        Calcula e retorna o percentual de produtos gratuitos e pagos.
        
        Returns:
            tuple: Percentual de produtos gratuitos e pagos.
        """
        total_produtos, produtos_gratuitos, produtos_pagos = 0, 0, 0
        
        with open(self.nome_arquivo, newline='', encoding="utf-8") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv, delimiter=",")
            for linha in leitor_csv:
                total_produtos += 1
                price = float(linha['Price'])
                if price == 0:
                    produtos_gratuitos += 1
                else:
                    produtos_pagos += 1

        percentual_gratuitos = (produtos_gratuitos / total_produtos) * 100
        percentual_pagos = (produtos_pagos / total_produtos) * 100

        return percentual_gratuitos, percentual_pagos

    def calcular_quantidade_jogos_ano(self):
        """
        Calcula e retorna a quantidade de jogos lançados por ano e o ano com mais lançamentos.
        
        Returns:
            tuple: Quantidade de jogos do ano mais frequente e o ano correspondente.
        """
        lista_anos = self._carregar_anos()
        maxima_contagem, maximo_ano = self._contar_e_retornar_maior(lista_anos)
        return maxima_contagem, maximo_ano

    def calcular_percentual_valores(self):
        """
        Calcula e retorna o valor médio pago pelos produtos.
        
        Returns:
            float: Valor médio pago, formatado com 2 casas decimais.
        """
        total_produtos, produtos_pagos, soma_valores_pagos = 0, 0, 0
        
        with open(self.nome_arquivo, newline='', encoding="utf-8") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv, delimiter=",")
            for linha in leitor_csv:
                total_produtos += 1
                price = float(linha['Price'])
                if price > 0:
                    produtos_pagos += 1
                    soma_valores_pagos += price

        valor_medio_pago = soma_valores_pagos / produtos_pagos if produtos_pagos > 0 else 0
        return round(valor_medio_pago, 2)

    def _carregar_anos(self):
        """
        Método privado para carregar os anos de lançamento dos jogos.
        
        Returns:
            list: Lista contendo os anos de lançamento dos jogos.
        """
        lista_anos = []

        with open(self.nome_arquivo, newline='', encoding="utf-8") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv, delimiter=",")
            for linha in leitor_csv:
                ano = linha['Release date'][-4:]
                lista_anos.append(ano)

        return lista_anos

    def _contar_e_retornar_maior(self, lista):
        """
        Método privado para contar os elementos de uma lista e retornar o mais frequente.
        
        Args:
            lista (list): Lista de elementos para contagem.
            
        Returns:
            tuple: Elemento mais frequente e sua contagem.
        """
        contador = Counter(lista)
        mais_comuns = contador.most_common(1)[0]
        return mais_comuns[1], mais_comuns[0]

# Exemplo de uso
Validacao = AnaliseSteam('C://Users//Joao Henrique//Desktop//Temp//steam_games.csv')
percentual_gratuitos, percentual_pagos = Validacao.calcular_percentual_tipos()
print(f'O percentual de produtos gratuitos é de: {percentual_gratuitos:.2f}%')
print(f'O percentual de produtos pagos é de: {percentual_pagos:.2f}%')

quantidade_jogos, ano = Validacao.calcular_quantidade_jogos_ano()
print(f'Ano com mais jogos lançados: {ano}, Total de jogos: {quantidade_jogos}')

valor_medio_pago = Validacao.calcular_percentual_valores()
print(f'Valor médio pago: {valor_medio_pago}')
