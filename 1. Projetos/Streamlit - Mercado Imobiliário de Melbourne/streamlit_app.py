import pandas            as pd
import streamlit         as st
import seaborn           as sns
import matplotlib.pyplot as plt
import base64

import folium
from streamlit_folium import folium_static

from PIL import Image
from io  import BytesIO

# Configurações do Streamlit
st.set_page_config(page_title='Mercado Imobiliário',
                   page_icon='./img/pag_icon.png',
                   layout="wide",
                   initial_sidebar_state='expanded')

# ========== ESTILO ==========
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)

# CSS Personalizado
def carregar_css():
    st.markdown("""
    <style>
    /* Melhorias visuais para o dashboard imobiliário */
    .stMetric { border-left: 5px solid #4f8bf9; padding-left: 1rem; }
    .stDataFrame { font-size: 14px; }
    .stSlider [data-baseweb="slider"] { padding: 0px 10px; }
    .stExpander [data-testid="stExpanderDetails"] { padding: 10px; }
    .leaflet-popup-content {
        font-family: Arial, sans-serif;
        min-width: 200px;
    }
    .leaflet-popup-content-wrapper {
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

carregar_css()

# ========== FUNÇÕES AUXILIARES ==========
@st.cache_data
def load_data():
    """Carrega automaticamente o dataset processado"""
    try:
        df = pd.read_csv('./data/melbourne_housing_portugues.csv')
        
        # Mensagem com efeito fade-out
        fade_out_html = """
        <div id="fade-out-message" style='
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            margin-bottom: 10px;
            animation: fadeOut 5s ease-in forwards;
        '>
            Dataset carregado com sucesso!
        </div>
        
        <style>
        @keyframes fadeOut {
            0% { opacity: 1; }
            70% { opacity: 0.5; height: 0.5; padding: 5; margin: 5; overflow: hidden; }
            100% { opacity: 0; height: 0; padding: 0; margin: 0; overflow: hidden; }
        }
        </style>
        """
        
        st.markdown(fade_out_html, unsafe_allow_html=True)
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

@st.cache_data
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Dados_Imobiliarios')
    return output.getvalue()

# ========== CARREGAMENTO DOS DADOS ==========
df = load_data()

# ========== HEADER DO DASHBOARD ==========
st.markdown("""
<h1 style='text-align: center; color: #2a3f5f;'>
    Mercado Imobiliário de Melbourne <br> (Austrália - 2016-2018) <br>
</h1>
""", unsafe_allow_html=True)

# Sidebar - Logo e Filtros
with st.sidebar:
    st.image(Image.open("./img/icon.png"), width=200)
    st.markdown("<h2 style='text-align: center;'>Filtros</h2>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: center; margin-bottom: -10px;'>Selecione uma região</h4>", unsafe_allow_html=True)

    region_options = ['Todas'] + sorted(df['Regiao'].unique().tolist())
    selected_region = st.selectbox(
        label="_",
        label_visibility="hidden",
        options=region_options,
        index=0
    )

# ========== VISUALIZAÇÃO DOS DADOS ==========
if not df.empty:
    # Filtragem inicial por região
    if selected_region != 'Todas':
        df_filtrado = df[df['Regiao'] == selected_region]
    else:
        df_filtrado = df.copy()

    # Métricas Rápidas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Imóveis", len(df_filtrado))
    with col2:
        st.metric("Imóveis Subvalorizados", df_filtrado['Subvalorizado'].sum())
    with col3:
        st.metric("Imóveis Supervalorizados", df_filtrado['Supervalorizado'].sum())

    # ========== MAPA INTERATIVO ==========
st.header("🌍 Mapa de Imóveis")

# Coordenadas de Melbourne como fallback
MELBOURNE_COORDS = {"latitude": -37.8136, "longitude": 144.9631}

# ========== SEÇÃO DE FILTROS ==========
with st.expander("🔧 Filtros Avançados", expanded=True):
    # Linha 1: Filtros temporais
    col1, col2 = st.columns(2)
    
    with col1:
        # Slider para Ano_Venda
        min_year = int(df_filtrado['Ano_Venda'].min())
        max_year = int(df_filtrado['Ano_Venda'].max())
        st.markdown('<style>div[data-testid="stSlider"] label {margin-bottom: 10px;}</style>', unsafe_allow_html=True)
        selected_years = st.slider(
            "Ano de Venda",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year),
            step=1
        )
    
    with col2:
        # Slider para Mes_Venda
        min_month = int(df_filtrado['Mes_Venda'].min())
        max_month = int(df_filtrado['Mes_Venda'].max())
        st.markdown('<style>div[data-testid="stSlider"] label {margin-bottom: 10px;}</style>', unsafe_allow_html=True)
        selected_months = st.slider(
            "Mês de Venda",
            min_value=min_month,
            max_value=max_month,
            value=(min_month, max_month),
            step=1
        )
    
    # Linha 2: Filtros de características
    col3, col4 = st.columns(2)
    
    with col3:
        # Slider para Vagas_Garagem
        min_garage = int(df_filtrado['Vagas_Garagem'].min())
        max_garage = int(df_filtrado['Vagas_Garagem'].max())
        st.markdown('<style>div[data-testid="stSlider"] label {margin-bottom: 10px;}</style>', unsafe_allow_html=True)
        selected_garage = st.slider(
            "Vagas de Garagem",
            min_value=min_garage,
            max_value=max_garage,
            value=(min_garage, max_garage),
            step=1
        )
    
    with col4:
        # Slider para Quartos
        min_rooms = int(df_filtrado['Quartos'].min())
        max_rooms = int(df_filtrado['Quartos'].max())
        st.markdown('<style>div[data-testid="stSlider"] label {margin-bottom: 10px;}</style>', unsafe_allow_html=True)
        selected_rooms = st.slider(
            "Quantidade de Quartos",
            min_value=min_rooms,
            max_value=max_rooms,
            value=(min_rooms, max_rooms),
            step=1
        )
    
    # Linha 3: Novos filtros adicionados
    col5, col6 = st.columns(2)
    
    with col5:
        # Slider para Distancia_CBD
        min_dist = float(df_filtrado['Distancia_CBD'].min())
        max_dist = float(df_filtrado['Distancia_CBD'].max())
        selected_dist = st.slider(
            "Distância do Centro (km)",
            min_value=min_dist,
            max_value=max_dist,
            value=(min_dist, max_dist),
            step=0.1,
            format="%.1f km"
        )
    
    with col6:
        # Selectbox para Corretor
        seller_options = ['Todos'] + sorted(df_filtrado['Corretor'].unique().tolist())
        selected_seller = st.selectbox(
            "Corretora",
            options=seller_options,
            index=0
        )
    
    col7, col8 = st.columns(2)
    
    with col7:
        # Slider para Idade_Imovel
        min_age = int(df_filtrado['Idade_Imovel'].min())
        max_age = int(df_filtrado['Idade_Imovel'].max())
        selected_age = st.slider(
            "Idade do Imóvel (anos)",
            min_value=min_age,
            max_value=max_age,
            value=(min_age, max_age),
            step=1
        )

    with col8:
        # Slider para Idade_Imovel
        st.markdown("Caso a aplicação esteja lenta é recomendado:\n* **Selecionar uma região** | **Filtrar por Valorização**\n* Fazer um café ☕\n* Tentar a versão [Pocket](https://ebac-semantix-1.onrender.com/) (30% do dataframe)")
        
    
    # Linha 5: Checkboxes para valorização
    st.markdown("**Filtrar por valorização:**")
    col9, col10, col11 = st.columns(3)
    
    with col9:
        show_normal = st.checkbox("Preço Adequado", value=True)
    
    with col10:
        show_under = st.checkbox("Subvalorizados", value=True)
    
    with col11:
        show_over = st.checkbox("Supervalorizados", value=True)

# ========== APLICAÇÃO DOS FILTROS ==========
# Aplicar filtro de região primeiro
if selected_region != 'Todas':
    df_filtrado = df[df['Regiao'] == selected_region].copy()
else:
    df_filtrado = df.copy()

# Aplicar filtros temporais e de características
df_filtrado = df_filtrado[
    (df_filtrado['Ano_Venda'].between(*selected_years)) &
    (df_filtrado['Mes_Venda'].between(*selected_months)) &
    (df_filtrado['Vagas_Garagem'].between(*selected_garage)) &
    (df_filtrado['Quartos'].between(*selected_rooms)) &
    (df_filtrado['Distancia_CBD'].between(*selected_dist)) &
    (df_filtrado['Idade_Imovel'].between(*selected_age))
]

# Aplicar filtro de corretor se selecionado
if selected_seller != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Corretor'] == selected_seller]

# Aplicar filtros de valorização
filter_conditions = []
if show_normal:
    filter_conditions.append((df_filtrado['Subvalorizado'] == False) & (df_filtrado['Supervalorizado'] == False))
if show_under:
    filter_conditions.append(df_filtrado['Subvalorizado'] == True)
if show_over:
    filter_conditions.append(df_filtrado['Supervalorizado'] == True)

# Combinar condições com OR se houver filtros selecionados
if filter_conditions:
    combined_condition = filter_conditions[0]
    for condition in filter_conditions[1:]:
        combined_condition = combined_condition | condition
    df_filtrado = df_filtrado[combined_condition]
else:
    st.warning("Selecione pelo menos um tipo de valorização para visualizar no mapa.")
    st.stop()

# ========== PREPARAÇÃO DO MAPA ==========
map_data = df_filtrado.copy()

# Verificar se há dados após os filtros
if map_data.empty:
    st.warning("Nenhum imóvel encontrado com os filtros atuais.")
    st.stop()

# Garantir coordenadas válidas
if 'Latitude' in map_data.columns and 'Longitude' in map_data.columns:
    map_data = map_data.rename(columns={
        'Latitude': 'latitude', 
        'Longitude': 'longitude'
    }).dropna(subset=['latitude', 'longitude'])
    
    if not map_data.empty:
        # Criar coluna de cor baseada no status de valorização
        map_data['color'] = map_data.apply(
            lambda x: "#556B2F" if x['Subvalorizado'] else ("#FF8C00" if x['Supervalorizado'] else "#5F9EA0"),
            axis=1
        )
        
        # Container para o mapa
        map_container = st.container()
        
        # Estado da sessão para controlar o zoom
        if 'map_zoom' not in st.session_state:
            st.session_state.map_zoom = 10  # Zoom padrão
        
        # Criar mapa Folium com tooltips
        with map_container:
            m = folium.Map(
                location=[MELBOURNE_COORDS["latitude"], MELBOURNE_COORDS["longitude"]],
                zoom_start=st.session_state.map_zoom
            )
            
            # Adicionar marcadores com popup
            for idx, row in map_data.iterrows():
    # Tradução dos tipos de imóvel
                tipo_traduzido = {
                    'br': 'quarto(s)',
                    'h': 'casa, chalé, vila, semi, terraço',
                    'u': 'unidade, duplex',
                    't': 'Casa Germinada',
                    'dev site': 'terreno para desenvolvimento',
                    'o res': 'outro tipo residencial'
                }.get(row['Tipo_Imovel'], row['Tipo_Imovel'])  # Usa o valor original se não estiver no dicionário
                
                # Link para o Google Maps
                google_maps_link = f"https://www.google.com.br/maps/@{row['latitude']},{row['longitude']},19z"
                
                popup_content = f"""
                <div style="font-family: Arial; min-width: 200px;">
                    <h4 style="margin-bottom: 5px; color: #2a3f5f;">Informações do Imóvel</h4>
                    <p><b>Tipo:</b> {tipo_traduzido}</p>
                    <p><b>Preço:</b> AUD ${row['Preco']:,.2f}</p>
                    <p><b>Data Venda:</b> {row['Data_Venda']}</p>
                    <p><b>Quartos:</b> {row['Quartos']}</p>
                    <p><b>Região:</b> {row['Regiao']}</p>
                    <p style="margin-top: 10px;">
                        <a href="{google_maps_link}" target="_blank" style="color: #1a73e8; text-decoration: none;">
                            <b>🔗 Link Google Maps</b>
                        </a>
                    </p>
                </div>
    """
                
                folium.CircleMarker(
                    location=[row['latitude'], row['longitude']],
                    radius=5,
                    color=row['color'],
                    fill=True,
                    fill_color=row['color'],
                    popup=folium.Popup(popup_content, max_width=300),
                    tooltip=f"Preço: AUD ${row['Preco']:,.2f}"
                ).add_to(m)
            
            # Exibir mapa
            folium_static(m, width=1000, height=600)
            
            # Botão para resetar o zoom
            if st.sidebar.button("Retornar para Melbourne", key="reset_map"):
                st.session_state.map_zoom = 10
                st.session_state.selected_region = 'Todas'
                st.rerun()
        
        # DataFrame recolhível
        with st.expander("🔍 Visualizar Dados Filtrados", expanded=False):
            st.dataframe(
                map_data.drop(columns=['color']),
                height=300,
                use_container_width=True
            )
        
        # Legenda
        st.sidebar.markdown("""
        **Legenda:**
        * <span style='color: cadetblue; font-weight: bold'>Preço Adequado</span>
        * <span style='color: #556B2F; font-weight: bold'>Subvalorizados</span>
        * <span style='color: DarkOrange; font-weight: bold'>Supervalorizados</span>
        """, unsafe_allow_html=True)

        with st.sidebar:
            # Divisor e seção pessoal
            st.markdown("<h2 style='text-align: center;'>Contato</h2>", unsafe_allow_html=True)
            # Seu nome centralizado
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <h3>Pedro Henrique</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Colunas para os ícones com links
            col1, col2 = st.columns(2)
            
            with col1:
                # Ícone do GitHub
                st.markdown("""
                <div style="text-align: center;">
                    <a href="https://github.com/PedroHenrique1704" target="_blank">
                        <img src="data:image/png;base64,{}" width="40">
                    </a>
                </div>
                """.format(base64.b64encode(open("./img/git.png", "rb").read()).decode()), 
                unsafe_allow_html=True)
            
            with col2:
                # Ícone do LinkedIn
                st.markdown("""
                <div style="text-align: center;">
                    <a href="https://www.linkedin.com/in/phcf/" target="_blank">
                        <img src="data:image/png;base64,{}" width="40">
                    </a>
                </div>
                """.format(base64.b64encode(open("./img/in.png", "rb").read()).decode()), 
                unsafe_allow_html=True)
            
            st.sidebar.markdown('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            st.sidebar.markdown("<p style='text-align: center; font-size: 14px; font-style: italic;'>Feito em 25/03/2025</p>", unsafe_allow_html=True)

    else:
        st.error("Não há coordenadas válidas para exibir o mapa.")
else:
    st.error("Colunas de latitude/longitude não encontradas.")