"""
Módulo para gerar dados de exemplo para o dashboard
Gera dados realistas de vendas/negócios
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def gerar_dados_vendas(n_registros=1000, seed=42):
    """
    Gera um dataset de vendas com dados realistas
    
    Args:
        n_registros: Número de registros a gerar
        seed: Seed para reprodutibilidade
    
    Returns:
        DataFrame com dados de vendas
    """
    np.random.seed(seed)
    random.seed(seed)
    
    # Categorias de produtos
    categorias = ['Eletrônicos', 'Roupas', 'Casa e Jardim', 'Esportes', 
                  'Livros', 'Brinquedos', 'Alimentos', 'Beleza']
    
    # Regiões
    regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    
    # Cidades por região
    cidades = {
        'Norte': ['Manaus', 'Belém', 'Porto Velho'],
        'Nordeste': ['Salvador', 'Recife', 'Fortaleza', 'Natal'],
        'Centro-Oeste': ['Brasília', 'Goiânia', 'Campo Grande'],
        'Sudeste': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Vitória'],
        'Sul': ['Curitiba', 'Porto Alegre', 'Florianópolis']
    }
    
    # Gerar datas (últimos 12 meses)
    data_inicio = datetime.now() - timedelta(days=365)
    datas = [data_inicio + timedelta(days=x) for x in range(n_registros)]
    datas = sorted(random.sample(datas, n_registros))
    
    # Gerar dados
    dados = []
    for i in range(n_registros):
        categoria = np.random.choice(categorias)
        regiao = np.random.choice(regioes)
        cidade = np.random.choice(cidades[regiao])
        
        # Preços variam por categoria
        precos_base = {
            'Eletrônicos': (500, 5000),
            'Roupas': (50, 500),
            'Casa e Jardim': (30, 800),
            'Esportes': (100, 1500),
            'Livros': (20, 150),
            'Brinquedos': (25, 400),
            'Alimentos': (10, 200),
            'Beleza': (15, 300)
        }
        
        preco_min, preco_max = precos_base[categoria]
        valor = round(np.random.uniform(preco_min, preco_max), 2)
        quantidade = np.random.randint(1, 10)
        total = round(valor * quantidade, 2)
        
        # Desconto aleatório (0-30%)
        desconto = np.random.choice([0, 5, 10, 15, 20, 25, 30], p=[0.3, 0.2, 0.15, 0.15, 0.1, 0.05, 0.05])
        valor_final = round(total * (1 - desconto/100), 2)
        
        # Status da venda
        status = np.random.choice(['Concluída', 'Pendente', 'Cancelada'], p=[0.85, 0.1, 0.05])
        
        # Método de pagamento
        metodo_pagamento = np.random.choice(['Cartão Crédito', 'Cartão Débito', 'PIX', 'Boleto'], 
                                           p=[0.4, 0.2, 0.3, 0.1])
        
        dados.append({
            'ID': f'V{i+1:05d}',
            'Data': datas[i],
            'Categoria': categoria,
            'Produto': f'Produto {categoria} {i+1}',
            'Região': regiao,
            'Cidade': cidade,
            'Valor_Unitário': valor,
            'Quantidade': quantidade,
            'Valor_Total': total,
            'Desconto_%': desconto,
            'Valor_Final': valor_final,
            'Status': status,
            'Método_Pagamento': metodo_pagamento,
            'Vendedor': f'Vendedor {np.random.randint(1, 21)}',
            'Cliente_ID': f'C{np.random.randint(1000, 9999)}'
        })
    
    df = pd.DataFrame(dados)
    
    # Adicionar colunas derivadas
    df['Mês'] = df['Data'].dt.to_period('M')
    df['Ano'] = df['Data'].dt.year
    df['Trimestre'] = df['Data'].dt.quarter
    df['Dia_Semana'] = df['Data'].dt.day_name()
    df['Mês_Nome'] = df['Data'].dt.strftime('%B')
    
    return df

def salvar_dados(df, caminho='data/vendas.csv'):
    """Salva o DataFrame em CSV"""
    import os
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_csv(caminho, index=False, encoding='utf-8-sig')
    print(f"Dados salvos em {caminho}")
    return caminho

if __name__ == "__main__":
    # Gerar e salvar dados
    print("Gerando dados de vendas...")
    df_vendas = gerar_dados_vendas(n_registros=2000)
    salvar_dados(df_vendas)
    print(f"\nDataset criado com {len(df_vendas)} registros")
    print(f"\nPrimeiras linhas:")
    print(df_vendas.head())
    print(f"\nInformações do dataset:")
    print(df_vendas.info())