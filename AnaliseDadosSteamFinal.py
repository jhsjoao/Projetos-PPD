import csv
import os
from collections import Counter

class AnaliseSteam:
    """Classe para análise de dados de jogos do Steam a partir de um arquivo CSV."""

    def __init__(self, arquivo):
        """
        Inicializa a classe com o caminho do arquivo CSV.
        
        Args:
            arquivo (str): Nome do arquivo CSV a ser analisado.
        """
        self.nome_arquivo = arquivo
        self.dados = self._carregar_dados()

    def _carregar_dados(self):
        """Carrega os dados do arquivo CSV e retorna uma lista de dicionários."""
        caminho_arquivo = os.path.join(os.path.dirname(__file__), self.nome_arquivo)
        
        try:
            with open(caminho_arquivo, newline='', encoding='utf-8') as arquivo_csv:
                return list(csv.DictReader(arquivo_csv, delimiter=","))
        except FileNotFoundError:
            print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
            return []
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
            return []

    def calcular_percentual_tipos(self):
        """Calcula o percentual de produtos gratuitos e pagos."""
        total_produtos = len(self.dados)
        if total_produtos == 0:
            return 0, 0

        produtos_gratuitos = sum(1 for linha in self.dados if float(linha['Price']) == 0)
        produtos_pagos = total_produtos - produtos_gratuitos

        percentual_gratuitos = (produtos_gratuitos / total_produtos) * 100
        percentual_pagos = (produtos_pagos / total_produtos) * 100

        return round(percentual_gratuitos, 2), round(percentual_pagos, 2)

    def calcular_quantidade_jogos_ano(self):
        """Calcula a quantidade de jogos lançados por ano."""
        lista_anos = [linha['Release date'][-4:].strip() for linha in self.dados if linha['Release date'][-4:].isdigit()]
        if not lista_anos:
            return 0, None

        contador = Counter(lista_anos)
        ano_mais_frequente, maxima_contagem = contador.most_common(1)[0]
        return maxima_contagem, ano_mais_frequente

    def calcular_media_valores_pagos(self):
        """Calcula o valor médio pago pelos produtos."""
        precos_pagos = [float(linha['Price']) for linha in self.dados if float(linha['Price']) > 0]
        if not precos_pagos:
            return 0.0
        
        valor_medio = sum(precos_pagos) / len(precos_pagos)
        return round(valor_medio, 2)


if __name__ == "__main__":
    # Usar o nome do arquivo CSV na mesma pasta do script
    nome_arquivo_csv = 'TesteDadosSteam.csv'
    analise = AnaliseSteam(nome_arquivo_csv)
    
    percentual_gratuitos, percentual_pagos = analise.calcular_percentual_tipos()
    print(f'O percentual de produtos gratuitos é de: {percentual_gratuitos:.2f}%')
    print(f'O percentual de produtos pagos é de: {percentual_pagos:.2f}%')
    
    quantidade_jogos, ano = analise.calcular_quantidade_jogos_ano()
    print(f'Ano com mais jogos lançados: {ano}, Total de jogos: {quantidade_jogos}')
    
    valor_medio_pago = analise.calcular_media_valores_pagos()
    print(f'Valor médio pago: {valor_medio_pago}')
