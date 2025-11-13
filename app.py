"""
Dashboard Profissional de Análise de Vendas
Aplicação Streamlit com análise avançada usando Pandas
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# Adicionar src ao path
src_path = os.path.join(os.path.dirname(__file__), 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from data_processor import DataProcessor
    from visualizations import Visualizations
except ImportError as e:
    st.error(f"Erro ao importar módulos: {e}")
    st.stop()

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados():
    """Carrega os dados do CSV ou gera automaticamente se não existir"""
    import os
    
    # Obter o diretório base do arquivo app.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_dados = os.path.join(base_dir, 'data', 'vendas.csv')
    
    # Verificar se o arquivo existe
    if not os.path.exists(caminho_dados):
        # Gerar dados automaticamente
        with st.spinner('Gerando dados de exemplo... Isso pode levar alguns segundos.'):
            try:
                from data_generator import gerar_dados_vendas, salvar_dados
                # Garantir que a pasta data existe
                os.makedirs(os.path.dirname(caminho_dados), exist_ok=True)
                df = gerar_dados_vendas(n_registros=2000)
                salvar_dados(df, caminho_dados)
                st.success(f'✅ Dados gerados com sucesso! ({len(df)} registros)')
            except Exception as e:
                st.error(f"Erro ao gerar dados: {e}")
                st.stop()
    else:
        # Carregar dados existentes
        try:
            df = pd.read_csv(caminho_dados, parse_dates=['Data'])
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            st.stop()
    
    return df

def main():
    """Função principal do dashboard"""
    
    # Header
    st.markdown('<h1 class="main-header">📊 Dashboard Profissional de Vendas</h1>', 
                unsafe_allow_html=True)
    
    # Carregar dados
    df_original = carregar_dados()
    
    # Sidebar - Filtros
    st.sidebar.header("🔍 Filtros")
    
    # Filtro de data
    st.sidebar.subheader("Período")
    data_min = df_original['Data'].min().date()
    data_max = df_original['Data'].max().date()
    
    data_inicio = st.sidebar.date_input(
        "Data Inicial",
        value=data_min,
        min_value=data_min,
        max_value=data_max
    )
    
    data_fim = st.sidebar.date_input(
        "Data Final",
        value=data_max,
        min_value=data_min,
        max_value=data_max
    )
    
    # Filtro de status
    st.sidebar.subheader("Status")
    status_options = df_original['Status'].unique().tolist()
    status_selecionados = st.sidebar.multiselect(
        "Selecione os status",
        options=status_options,
        default=status_options
    )
    
    # Filtro de categoria
    st.sidebar.subheader("Categoria")
    categorias = df_original['Categoria'].unique().tolist()
    categorias_selecionadas = st.sidebar.multiselect(
        "Selecione as categorias",
        options=categorias,
        default=categorias
    )
    
    # Filtro de região
    st.sidebar.subheader("Região")
    regioes = df_original['Região'].unique().tolist()
    regioes_selecionadas = st.sidebar.multiselect(
        "Selecione as regiões",
        options=regioes,
        default=regioes
    )
    
    # Aplicar filtros
    processor = DataProcessor(df_original)
    processor.filtrar_por_periodo(data_inicio, data_fim)
    processor.filtrar_por_status(status_selecionados)
    processor.filtrar_por_categoria(categorias_selecionadas)
    processor.filtrar_por_regiao(regioes_selecionadas)
    
    df_filtrado = processor.get_dataframe()
    
    # Métricas principais
    st.header("📈 Métricas Principais")
    
    metricas = processor.calcular_metricas_vendas()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Receita Total",
            value=f"R$ {metricas['receita_total']:,.2f}",
            delta=f"R$ {metricas['receita_total']:,.2f}"
        )
    
    with col2:
        st.metric(
            label="🛒 Total de Vendas",
            value=f"{metricas['total_vendas']:,}",
            delta=f"{metricas['total_vendas']:,}"
        )
    
    with col3:
        st.metric(
            label="💵 Ticket Médio",
            value=f"R$ {metricas['ticket_medio']:,.2f}",
            delta=f"R$ {metricas['ticket_mediano']:,.2f}"
        )
    
    with col4:
        st.metric(
            label="📦 Total de Produtos",
            value=f"{metricas['total_produtos']:,}",
            delta=f"{metricas['total_produtos']:,}"
        )
    
    # Segunda linha de métricas
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.metric(
            label="❌ Vendas Canceladas",
            value=f"{metricas['vendas_canceladas']:,}"
        )
    
    with col6:
        st.metric(
            label="⏳ Vendas Pendentes",
            value=f"{metricas['vendas_pendentes']:,}"
        )
    
    with col7:
        st.metric(
            label="🎯 Desconto Médio",
            value=f"{metricas['desconto_medio']:.1f}%"
        )
    
    with col8:
        st.metric(
            label="📊 Registros Filtrados",
            value=f"{len(df_filtrado):,}"
        )
    
    st.divider()
    
    # Análises e Gráficos
    st.header("📊 Análises e Visualizações")
    
    # Tabs para organizar os gráficos
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Temporal", "🏷️ Categorias", "🌎 Regiões", 
        "👥 Vendedores", "💳 Pagamentos"
    ])
    
    with tab1:
        st.subheader("Análise Temporal")
        
        col1, col2 = st.columns(2)
        
        with col1:
            viz = Visualizations()
            fig_temporal = viz.grafico_receita_temporal(df_filtrado, periodo='M')
            st.plotly_chart(fig_temporal, use_container_width=True)
        
        with col2:
            fig_tendencia = viz.grafico_tendencia_mensal(df_filtrado)
            st.plotly_chart(fig_tendencia, use_container_width=True)
        
        # Tabela de análise temporal
        st.subheader("Resumo Mensal")
        analise_temporal = processor.analise_temporal(periodo='M')
        st.dataframe(analise_temporal, use_container_width=True)
    
    with tab2:
        st.subheader("Análise por Categoria")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_categoria = viz.grafico_receita_por_categoria(df_filtrado)
            st.plotly_chart(fig_categoria, use_container_width=True)
        
        with col2:
            fig_pizza = viz.grafico_pizza_categorias(df_filtrado)
            st.plotly_chart(fig_pizza, use_container_width=True)
        
        # Tabela de análise por categoria
        st.subheader("Detalhamento por Categoria")
        analise_categoria = processor.analise_por_categoria()
        st.dataframe(analise_categoria, use_container_width=True)
    
    with tab3:
        st.subheader("Análise por Região")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_regiao = viz.grafico_receita_por_regiao(df_filtrado)
            st.plotly_chart(fig_regiao, use_container_width=True)
        
        with col2:
            fig_heatmap = viz.mapa_calor_vendas(df_filtrado)
            st.plotly_chart(fig_heatmap, use_container_width=True)
        
        # Tabela de análise por região
        st.subheader("Detalhamento por Região")
        analise_regiao = processor.analise_por_regiao()
        st.dataframe(analise_regiao, use_container_width=True)
    
    with tab4:
        st.subheader("Análise de Vendedores")
        
        n_vendedores = st.slider("Número de vendedores a exibir", 5, 20, 10)
        
        fig_vendedores = viz.grafico_top_vendedores(df_filtrado, n=n_vendedores)
        st.plotly_chart(fig_vendedores, use_container_width=True)
        
        # Tabela de top vendedores
        st.subheader(f"Top {n_vendedores} Vendedores")
        top_vendedores = processor.top_vendedores(n=n_vendedores)
        st.dataframe(top_vendedores, use_container_width=True)
    
    with tab5:
        st.subheader("Análise de Métodos de Pagamento")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_pagamento = viz.grafico_metodo_pagamento(df_filtrado)
            st.plotly_chart(fig_pagamento, use_container_width=True)
        
        with col2:
            fig_status = viz.grafico_vendas_por_status(df_filtrado)
            st.plotly_chart(fig_status, use_container_width=True)
        
        # Tabela de métodos de pagamento
        st.subheader("Detalhamento por Método de Pagamento")
        analise_pagamento = processor.analise_metodo_pagamento()
        st.dataframe(analise_pagamento, use_container_width=True)
    
    st.divider()
    
    # Tabela de dados
    st.header("📋 Dados Detalhados")
    
    st.subheader(f"Registros: {len(df_filtrado):,}")
    
    # Opções de visualização
    col1, col2 = st.columns(2)
    
    with col1:
        colunas_selecionadas = st.multiselect(
            "Selecione as colunas para exibir",
            options=df_filtrado.columns.tolist(),
            default=df_filtrado.columns.tolist()[:10]
        )
    
    with col2:
        n_linhas = st.slider("Número de linhas", 10, 1000, 100)
    
    if colunas_selecionadas:
        st.dataframe(
            df_filtrado[colunas_selecionadas].head(n_linhas),
            use_container_width=True,
            height=400
        )
    
    # Estatísticas descritivas
    st.subheader("📊 Estatísticas Descritivas")
    
    col_numericas = df_filtrado.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if col_numericas:
        st.dataframe(df_filtrado[col_numericas].describe(), use_container_width=True)
    
    # Tendências
    st.divider()
    st.header("📈 Tendências e Insights")
    
    tendencias = processor.tendencias()
    
    if tendencias:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Crescimento Mensal",
                f"{tendencias.get('crescimento_mensal', 0):.2f}%"
            )
        
        with col2:
            st.metric(
                "Tendência",
                tendencias.get('tendencia', 'N/A')
            )
        
        with col3:
            st.metric(
                "Último Mês",
                f"R$ {tendencias.get('ultimo_mes', 0):,.2f}"
            )
    
    # Footer
    st.divider()
    st.markdown(
        """
        <div style='text-align: center; color: gray; padding: 20px;'>
            <p>Dashboard Profissional de Análise de Vendas | Desenvolvido com Pandas, Streamlit e Plotly</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()