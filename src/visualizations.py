"""
Módulo para visualizações profissionais
Utiliza matplotlib, seaborn e plotly para gráficos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuração de estilo
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class Visualizations:
    """Classe para criar visualizações profissionais"""
    
    @staticmethod
    def grafico_receita_temporal(df, periodo='M'):
        """
        Gráfico de linha mostrando receita ao longo do tempo
        
        Args:
            df: DataFrame com coluna 'Data' e 'Valor_Final'
            periodo: Período de agregação ('D', 'W', 'M')
        """
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        df_vendas = df_vendas.set_index('Data')
        
        receita_temporal = df_vendas.resample(periodo)['Valor_Final'].sum()
        
        fig = px.line(
            x=receita_temporal.index,
            y=receita_temporal.values,
            title='Receita ao Longo do Tempo',
            labels={'x': 'Período', 'y': 'Receita (R$)'},
            markers=True
        )
        
        fig.update_layout(
            xaxis_title="Período",
            yaxis_title="Receita (R$)",
            hovermode='x unified',
            template='plotly_white',
            height=400
        )
        
        return fig
    
    @staticmethod
    def grafico_receita_por_categoria(df):
        """Gráfico de barras horizontal com receita por categoria"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        receita_categoria = df_vendas.groupby('Categoria')['Valor_Final'].sum().sort_values(ascending=True)
        
        fig = px.bar(
            x=receita_categoria.values,
            y=receita_categoria.index,
            orientation='h',
            title='Receita por Categoria',
            labels={'x': 'Receita (R$)', 'y': 'Categoria'},
            color=receita_categoria.values,
            color_continuous_scale='Blues'
        )
        
        fig.update_layout(
            xaxis_title="Receita (R$)",
            yaxis_title="Categoria",
            template='plotly_white',
            height=400,
            showlegend=False
        )
        
        return fig
    
    @staticmethod
    def grafico_pizza_categorias(df):
        """Gráfico de pizza mostrando distribuição por categoria"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        receita_categoria = df_vendas.groupby('Categoria')['Valor_Final'].sum()
        
        fig = px.pie(
            values=receita_categoria.values,
            names=receita_categoria.index,
            title='Distribuição de Receita por Categoria',
            hole=0.4
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(template='plotly_white', height=400)
        
        return fig
    
    @staticmethod
    def grafico_receita_por_regiao(df):
        """Gráfico de barras com receita por região"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        receita_regiao = df_vendas.groupby('Região')['Valor_Final'].sum().sort_values(ascending=False)
        
        fig = px.bar(
            x=receita_regiao.index,
            y=receita_regiao.values,
            title='Receita por Região',
            labels={'x': 'Região', 'y': 'Receita (R$)'},
            color=receita_regiao.values,
            color_continuous_scale='Viridis'
        )
        
        fig.update_layout(
            xaxis_title="Região",
            yaxis_title="Receita (R$)",
            template='plotly_white',
            height=400,
            showlegend=False
        )
        
        return fig
    
    @staticmethod
    def mapa_calor_vendas(df):
        """Mapa de calor mostrando vendas por categoria e região"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        pivot = df_vendas.pivot_table(
            values='Valor_Final',
            index='Categoria',
            columns='Região',
            aggfunc='sum',
            fill_value=0
        )
        
        fig = px.imshow(
            pivot.values,
            labels=dict(x="Região", y="Categoria", color="Receita (R$)"),
            x=pivot.columns,
            y=pivot.index,
            title='Mapa de Calor: Receita por Categoria e Região',
            color_continuous_scale='YlOrRd',
            aspect="auto"
        )
        
        fig.update_layout(template='plotly_white', height=500)
        
        return fig
    
    @staticmethod
    def grafico_vendas_por_status(df):
        """Gráfico de barras mostrando vendas por status"""
        status_count = df['Status'].value_counts()
        
        fig = px.bar(
            x=status_count.index,
            y=status_count.values,
            title='Vendas por Status',
            labels={'x': 'Status', 'y': 'Quantidade'},
            color=status_count.values,
            color_continuous_scale='RdYlGn'
        )
        
        fig.update_layout(
            xaxis_title="Status",
            yaxis_title="Quantidade de Vendas",
            template='plotly_white',
            height=350,
            showlegend=False
        )
        
        return fig
    
    @staticmethod
    def grafico_metodo_pagamento(df):
        """Gráfico de pizza mostrando métodos de pagamento"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        metodo_count = df_vendas['Método_Pagamento'].value_counts()
        
        fig = px.pie(
            values=metodo_count.values,
            names=metodo_count.index,
            title='Distribuição por Método de Pagamento',
            hole=0.3
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(template='plotly_white', height=400)
        
        return fig
    
    @staticmethod
    def grafico_top_vendedores(df, n=10):
        """Gráfico de barras com top vendedores"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        top_vendedores = df_vendas.groupby('Vendedor')['Valor_Final'].sum().sort_values(ascending=False).head(n)
        
        fig = px.bar(
            x=top_vendedores.index,
            y=top_vendedores.values,
            title=f'Top {n} Vendedores',
            labels={'x': 'Vendedor', 'y': 'Receita (R$)'},
            color=top_vendedores.values,
            color_continuous_scale='Greens'
        )
        
        fig.update_layout(
            xaxis_title="Vendedor",
            yaxis_title="Receita (R$)",
            template='plotly_white',
            height=400,
            showlegend=False,
            xaxis={'tickangle': -45}
        )
        
        return fig
    
    @staticmethod
    def grafico_tendencia_mensal(df):
        """Gráfico de linha mostrando tendência mensal"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        df_vendas['Mês_Ano'] = df_vendas['Data'].dt.to_period('M')
        receita_mensal = df_vendas.groupby('Mês_Ano')['Valor_Final'].sum()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=receita_mensal.index.astype(str),
            y=receita_mensal.values,
            mode='lines+markers',
            name='Receita',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        
        # Adicionar linha de tendência
        if len(receita_mensal) > 1:
            z = np.polyfit(range(len(receita_mensal)), receita_mensal.values, 1)
            p = np.poly1d(z)
            fig.add_trace(go.Scatter(
                x=receita_mensal.index.astype(str),
                y=p(range(len(receita_mensal))),
                mode='lines',
                name='Tendência',
                line=dict(color='red', width=2, dash='dash')
            ))
        
        fig.update_layout(
            title='Tendência de Receita Mensal',
            xaxis_title="Mês",
            yaxis_title="Receita (R$)",
            template='plotly_white',
            height=400,
            hovermode='x unified'
        )
        
        return fig
    
    @staticmethod
    def dashboard_completo(df):
        """Cria um dashboard completo com múltiplos gráficos"""
        df_vendas = df[df['Status'] == 'Concluída'].copy()
        
        # Criar subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Receita por Categoria', 'Receita por Região', 
                          'Vendas Mensais', 'Top 5 Vendedores'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "scatter"}, {"type": "bar"}]]
        )
        
        # Receita por categoria
        receita_cat = df_vendas.groupby('Categoria')['Valor_Final'].sum().sort_values(ascending=True)
        fig.add_trace(
            go.Bar(x=receita_cat.values, y=receita_cat.index, orientation='h', name='Categoria'),
            row=1, col=1
        )
        
        # Receita por região
        receita_reg = df_vendas.groupby('Região')['Valor_Final'].sum()
        fig.add_trace(
            go.Bar(x=receita_reg.index, y=receita_reg.values, name='Região'),
            row=1, col=2
        )
        
        # Vendas mensais
        df_vendas['Mês_Ano'] = df_vendas['Data'].dt.to_period('M')
        receita_mensal = df_vendas.groupby('Mês_Ano')['Valor_Final'].sum()
        fig.add_trace(
            go.Scatter(x=receita_mensal.index.astype(str), y=receita_mensal.values, 
                      mode='lines+markers', name='Mensal'),
            row=2, col=1
        )
        
        # Top vendedores
        top_vend = df_vendas.groupby('Vendedor')['Valor_Final'].sum().sort_values(ascending=False).head(5)
        fig.add_trace(
            go.Bar(x=top_vend.index, y=top_vend.values, name='Vendedores'),
            row=2, col=2
        )
        
        fig.update_layout(
            height=800,
            title_text="Dashboard Completo de Vendas",
            template='plotly_white',
            showlegend=False
        )
        
        return fig