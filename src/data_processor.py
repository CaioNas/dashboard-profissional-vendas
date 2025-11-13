"""
Módulo para processamento e análise de dados com Pandas
Contém funções profissionais para análise de dados
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataProcessor:
    """Classe para processamento avançado de dados"""
    
    def __init__(self, df):
        """
        Inicializa o processador com um DataFrame
        
        Args:
            df: DataFrame do pandas
        """
        self.df = df.copy()
        self.df_original = df.copy()
    
    def limpar_dados(self):
        """Remove duplicatas e valores nulos críticos"""
        print(f"Registros antes da limpeza: {len(self.df)}")
        
        # Remover duplicatas
        self.df = self.df.drop_duplicates()
        
        # Remover registros com valores críticos nulos
        colunas_criticas = ['Data', 'Valor_Final', 'Status']
        self.df = self.df.dropna(subset=colunas_criticas)
        
        print(f"Registros após limpeza: {len(self.df)}")
        return self
    
    def filtrar_por_periodo(self, data_inicio=None, data_fim=None):
        """
        Filtra dados por período
        
        Args:
            data_inicio: Data inicial (datetime, date ou string)
            data_fim: Data final (datetime, date ou string)
        """
        if 'Data' in self.df.columns:
            if data_inicio:
                # Converter para datetime usando pd.to_datetime que aceita date, datetime, string, etc.
                data_inicio = pd.to_datetime(data_inicio)
                self.df = self.df[self.df['Data'] >= data_inicio]
            
            if data_fim:
                # Converter para datetime
                data_fim = pd.to_datetime(data_fim)
                # Adicionar 23:59:59.999 para incluir o dia inteiro
                data_fim = data_fim + pd.Timedelta(days=1) - pd.Timedelta(milliseconds=1)
                self.df = self.df[self.df['Data'] <= data_fim]
        
        return self
    
    def filtrar_por_status(self, status=None):
        """Filtra por status da venda"""
        if status and 'Status' in self.df.columns:
            if isinstance(status, list):
                self.df = self.df[self.df['Status'].isin(status)]
            else:
                self.df = self.df[self.df['Status'] == status]
        return self
    
    def filtrar_por_categoria(self, categorias=None):
        """Filtra por categorias"""
        if categorias and 'Categoria' in self.df.columns:
            if isinstance(categorias, list):
                self.df = self.df[self.df['Categoria'].isin(categorias)]
            else:
                self.df = self.df[self.df['Categoria'] == categorias]
        return self
    
    def filtrar_por_regiao(self, regioes=None):
        """Filtra por regiões"""
        if regioes and 'Região' in self.df.columns:
            if isinstance(regioes, list):
                self.df = self.df[self.df['Região'].isin(regioes)]
            else:
                self.df = self.df[self.df['Região'] == regioes]
        return self
    
    def reset_filtros(self):
        """Reseta todos os filtros"""
        self.df = self.df_original.copy()
        return self
    
    def calcular_metricas_vendas(self):
        """
        Calcula métricas principais de vendas
        
        Returns:
            dict com métricas calculadas
        """
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return {
                'total_vendas': 0,
                'receita_total': 0,
                'ticket_medio': 0,
                'total_produtos': 0,
                'vendas_canceladas': 0,
                'vendas_pendentes': 0,
                'ticket_mediano': 0,
                'receita_maxima': 0,
                'receita_minima': 0,
                'desconto_medio': 0
            }
        
        metricas = {
            'total_vendas': len(df_vendas),
            'receita_total': df_vendas['Valor_Final'].sum(),
            'ticket_medio': df_vendas['Valor_Final'].mean(),
            'ticket_mediano': df_vendas['Valor_Final'].median(),
            'total_produtos': df_vendas['Quantidade'].sum(),
            'vendas_canceladas': len(self.df[self.df['Status'] == 'Cancelada']),
            'vendas_pendentes': len(self.df[self.df['Status'] == 'Pendente']),
            'receita_maxima': df_vendas['Valor_Final'].max(),
            'receita_minima': df_vendas['Valor_Final'].min(),
            'desconto_medio': df_vendas['Desconto_%'].mean()
        }
        
        return metricas
    
    def analise_por_categoria(self):
        """Análise agregada por categoria"""
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return pd.DataFrame()
        
        analise = df_vendas.groupby('Categoria').agg({
            'Valor_Final': ['sum', 'mean', 'count'],
            'Quantidade': 'sum',
            'Desconto_%': 'mean'
        }).round(2)
        
        analise.columns = ['Receita_Total', 'Ticket_Medio', 'Num_Vendas', 
                          'Total_Produtos', 'Desconto_Medio']
        analise = analise.sort_values('Receita_Total', ascending=False)
        
        return analise
    
    def analise_por_regiao(self):
        """Análise agregada por região"""
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return pd.DataFrame()
        
        analise = df_vendas.groupby('Região').agg({
            'Valor_Final': ['sum', 'mean', 'count'],
            'Cidade': 'nunique'
        }).round(2)
        
        analise.columns = ['Receita_Total', 'Ticket_Medio', 'Num_Vendas', 'Num_Cidades']
        analise = analise.sort_values('Receita_Total', ascending=False)
        
        return analise
    
    def analise_temporal(self, periodo='M'):
        """
        Análise temporal das vendas
        
        Args:
            periodo: 'D' (dia), 'W' (semana), 'M' (mês), 'Q' (trimestre)
        """
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return pd.DataFrame()
        
        df_vendas = df_vendas.set_index('Data')
        
        analise = df_vendas.resample(periodo).agg({
            'Valor_Final': ['sum', 'mean', 'count'],
            'Quantidade': 'sum'
        }).round(2)
        
        analise.columns = ['Receita_Total', 'Ticket_Medio', 'Num_Vendas', 'Total_Produtos']
        analise = analise.fillna(0)
        
        return analise
    
    def top_vendedores(self, n=10):
        """Retorna os top N vendedores"""
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return pd.DataFrame()
        
        top = df_vendas.groupby('Vendedor').agg({
            'Valor_Final': ['sum', 'mean', 'count']
        }).round(2)
        
        top.columns = ['Receita_Total', 'Ticket_Medio', 'Num_Vendas']
        top = top.sort_values('Receita_Total', ascending=False).head(n)
        
        return top
    
    def analise_metodo_pagamento(self):
        """Análise por método de pagamento"""
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return pd.DataFrame()
        
        analise = df_vendas.groupby('Método_Pagamento').agg({
            'Valor_Final': ['sum', 'mean', 'count']
        }).round(2)
        
        analise.columns = ['Receita_Total', 'Ticket_Medio', 'Num_Transacoes']
        analise['Percentual'] = (analise['Receita_Total'] / analise['Receita_Total'].sum() * 100).round(2)
        analise = analise.sort_values('Receita_Total', ascending=False)
        
        return analise
    
    def tendencias(self):
        """Calcula tendências e crescimento"""
        df_vendas = self.df[self.df['Status'] == 'Concluída'].copy()
        
        if len(df_vendas) == 0:
            return {}
        
        # Análise mensal
        df_vendas['Mês'] = df_vendas['Data'].dt.to_period('M')
        df_mensal = df_vendas.groupby('Mês')['Valor_Final'].sum().sort_index()
        
        if len(df_mensal) < 2:
            return {'crescimento_mensal': 0, 'tendencia': 'Insuficiente'}
        
        # Calcular crescimento
        crescimento = ((df_mensal.iloc[-1] - df_mensal.iloc[-2]) / df_mensal.iloc[-2] * 100) if len(df_mensal) >= 2 else 0
        
        # Determinar tendência
        if crescimento > 5:
            tendencia = 'Crescimento Forte'
        elif crescimento > 0:
            tendencia = 'Crescimento Moderado'
        elif crescimento > -5:
            tendencia = 'Estável'
        else:
            tendencia = 'Declínio'
        
        return {
            'crescimento_mensal': round(crescimento, 2),
            'tendencia': tendencia,
            'ultimo_mes': float(df_mensal.iloc[-1]),
            'penultimo_mes': float(df_mensal.iloc[-2]) if len(df_mensal) >= 2 else 0
        }
    
    def get_dataframe(self):
        """Retorna o DataFrame atual"""
        return self.df.copy()