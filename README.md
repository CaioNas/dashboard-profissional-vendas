# 📊 Dashboard Profissional de Análise de Vendas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Dashboard interativo e profissional para análise avançada de dados de vendas com visualizações dinâmicas e insights em tempo real**

[🚀 Funcionalidades](#-funcionalidades) • [📦 Instalação](#-instalação) • [💻 Uso](#-uso) • [🛠️ Tecnologias](#️-tecnologias) • [📈 Demonstração](#-demonstração)

</div>

---

## 📌 Sobre o Projeto

Este projeto é um **dashboard profissional de análise de vendas** desenvolvido com Python, que permite visualizar, analisar e extrair insights valiosos de dados de vendas de forma interativa e intuitiva.

### 🎯 Objetivo

Criar uma ferramenta completa de Business Intelligence que transforma dados brutos de vendas em informações acionáveis, facilitando a tomada de decisões estratégicas para empresas e equipes de vendas.

### 🔍 Problema que Resolve

- **Análise manual demorada**: Elimina a necessidade de processar dados manualmente em planilhas
- **Visualizações estáticas**: Substitui gráficos estáticos por visualizações interativas e dinâmicas
- **Falta de insights**: Fornece análises automáticas de tendências, crescimento e performance
- **Dificuldade de filtragem**: Permite filtrar dados por múltiplos critérios simultaneamente
- **Análise fragmentada**: Centraliza todas as análises em um único dashboard

### 👥 Para Quem é Este Projeto

- ✅ **Analistas de Dados** que precisam de ferramentas profissionais de análise
- ✅ **Gestores de Vendas** que querem acompanhar performance e métricas
- ✅ **Estudantes** aprendendo análise de dados com Pandas e visualizações
- ✅ **Desenvolvedores** interessados em criar dashboards interativos
- ✅ **Empresas** que buscam soluções de Business Intelligence

### 📊 Nível do Projeto

**Intermediário a Avançado** - Combina conceitos de análise de dados, visualizações interativas e desenvolvimento de aplicações web.

---

## ✨ Funcionalidades

### 📈 Métricas em Tempo Real
- 💰 Receita Total
- 🛒 Total de Vendas
- 💵 Ticket Médio e Mediano
- 📦 Total de Produtos Vendidos
- ❌ Vendas Canceladas/Pendentes
- 🎯 Desconto Médio

### 🔍 Filtros Avançados
- 📅 **Filtro por Período**: Selecione datas inicial e final
- ✅ **Filtro por Status**: Concluída, Pendente, Cancelada
- 🏷️ **Filtro por Categoria**: Filtre por categorias de produtos
- 🌎 **Filtro por Região**: Análise geográfica das vendas

### 📊 Visualizações Interativas

#### 📈 Análise Temporal
- Gráfico de linha mostrando receita ao longo do tempo
- Tendência mensal com linha de regressão
- Resumo mensal detalhado

#### 🏷️ Análise por Categoria
- Gráfico de barras horizontal
- Gráfico de pizza (distribuição percentual)
- Tabela com métricas detalhadas por categoria

#### 🌎 Análise por Região
- Gráfico de barras por região
- Mapa de calor (categoria x região)
- Detalhamento por cidade

#### 👥 Análise de Vendedores
- Top N vendedores (configurável)
- Receita total e ticket médio por vendedor
- Número de vendas realizadas

#### 💳 Análise de Pagamentos
- Distribuição por método de pagamento
- Vendas por status
- Percentuais e valores detalhados

### 📋 Dados Detalhados
- Tabela interativa com todos os registros
- Seleção personalizada de colunas
- Estatísticas descritivas automáticas
- Exportação de dados filtrados

### 📈 Insights e Tendências
- Cálculo automático de crescimento mensal
- Identificação de tendências (Crescimento Forte, Moderado, Estável, Declínio)
- Comparação entre períodos

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.8+ | Linguagem principal |
| **Pandas** | 2.0+ | Manipulação e análise de dados |
| **Streamlit** | 1.28+ | Framework para aplicação web |
| **Plotly** | 5.17+ | Visualizações interativas |
| **NumPy** | 1.24+ | Operações numéricas |
| **Matplotlib** | 3.7+ | Visualizações adicionais |
| **Seaborn** | 0.12+ | Estatísticas e gráficos estatísticos |

---

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/CaioNas/dashboard-profissional-vendas.git
   cd dashboard-profissional-vendas
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Gere os dados de exemplo (se necessário)**
   ```bash
   python src/data_generator.py
   ```
   
   > **Nota**: O dashboard gera os dados automaticamente na primeira execução se não existirem.

5. **Execute o dashboard**
   ```bash
   streamlit run app.py
   ```

6. **Acesse no navegador**
   ```
   http://localhost:8501
   ```

---

## 💻 Uso

### Iniciando o Dashboard

Após a instalação, execute:

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no seu navegador.

### Navegando pelo Dashboard

1. **Filtros (Barra Lateral Esquerda)**
   - Use os filtros para refinar sua análise
   - Selecione período, status, categorias e regiões
   - Os gráficos e métricas são atualizados automaticamente

2. **Métricas Principais**
   - Visualize os KPIs principais no topo da página
   - Métricas são calculadas em tempo real com base nos filtros

3. **Abas de Análise**
   - **Temporal**: Análise ao longo do tempo
   - **Categorias**: Performance por categoria
   - **Regiões**: Análise geográfica
   - **Vendedores**: Top performers
   - **Pagamentos**: Métodos de pagamento

4. **Interatividade**
   - Passe o mouse sobre os gráficos para ver detalhes
   - Use os controles para zoom e pan
   - Clique nas legendas para mostrar/ocultar séries

---

## 🏗️ Estrutura do Projeto

```
dashboard-profissional-vendas/
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
├── LICENSE                     # Licença MIT
├── .gitignore                  # Arquivos ignorados pelo Git
├── data/
│   └── vendas.csv              # Dataset de vendas (gerado automaticamente)
└── src/
    ├── __init__.py
    ├── data_generator.py      # Gerador de dados de exemplo
    ├── data_processor.py      # Processamento avançado com Pandas
    └── visualizations.py      # Módulo de visualizações
```

---

## 🔧 Como Funciona

### Arquitetura do Projeto

O projeto é dividido em módulos especializados:

#### 1. **Data Generator** (`data_generator.py`)
- Gera dados realistas de vendas
- Cria dataset com múltiplas dimensões (categoria, região, vendedor, etc.)
- Configurável (número de registros, seed para reprodutibilidade)

#### 2. **Data Processor** (`data_processor.py`)
- Classe `DataProcessor` para processamento avançado
- Métodos de filtragem (período, status, categoria, região)
- Cálculo de métricas e KPIs
- Análises agregadas e tendências

#### 3. **Visualizations** (`visualizations.py`)
- Classe `Visualizations` com métodos de gráficos
- Gráficos interativos com Plotly
- Múltiplos tipos de visualização (linha, barras, pizza, mapa de calor)

#### 4. **App Principal** (`app.py`)
- Interface Streamlit
- Integração de todos os módulos
- Layout responsivo e profissional

### Fluxo de Dados

```
Dados CSV → DataProcessor → Filtros → Métricas/Análises → Visualizations → Dashboard
```

---

## 🔮 Melhorias Futuras

### Versão 2.0 (Planejado)
- [ ] Conexão com banco de dados real (PostgreSQL, MySQL)
- [ ] Autenticação de usuários
- [ ] Exportação de relatórios em PDF
- [ ] Alertas automáticos por email
- [ ] Dashboard mobile responsivo
- [ ] Integração com APIs externas
- [ ] Machine Learning para previsões

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido com ❤️ usando Python, Pandas, Streamlit e Plotly

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Made with ❤️ and Python

</div>