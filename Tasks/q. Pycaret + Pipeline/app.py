import streamlit as st
import pandas as pd
from pycaret.classification import *
import tempfile
import os
from datetime import datetime
import base64
from PIL import Image

# Carrega o CSS personalizado
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Arquivo CSS não encontrado. Usando estilo padrão.")

# Configuração da página
st.set_page_config(page_title="Avaliação de Modelo de Credit Scoring", 
                   page_icon='./img/pag_icon.png',
                   layout="wide")

st.markdown("""
    <h2 style='text-align: center;'>📊 Avaliação de Modelo de Credit Scoring</h2>
""", unsafe_allow_html=True)


st.sidebar.image(Image.open("./img/icon.png"), width=200)


# Carrega o CSS personalizado
local_css('css/estilo.css')

# Barra lateral
with st.sidebar:
    st.markdown("---")
    st.header("⚙️ Parâmetros")
    uploaded_file = st.file_uploader("Carregar dataset (.ftr ou .pkl)", type=['ftr', 'pkl'])
    use_sample = st.checkbox("Usar dados de amostra\n (20% do arquivo)", value=True)
    threshold = st.slider("Limite para categorias raras", 0.01, 0.10, 0.05, 0.01)
    
    st.subheader("Parâmetros do Modelo")
    train_size = st.slider("Tamanho do treino", 0.5, 0.9, 0.8, 0.05)
    outliers_threshold = st.slider("Limite para outliers", 0.01, 0.10, 0.05, 0.01)
    
    run_button = st.button("Executar Avaliação do Modelo")
    st.markdown("---")

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

def save_plot(plot_name):
    try:
        with open(f"{plot_name}.png", "rb") as file:
            btn = st.download_button(
                label=f"💾 Baixar {plot_name.replace('_', ' ').title()}",
                data=file,
                file_name=f"{plot_name}.png",
                mime="image/png",
                on_click="ignore"
            )
    except FileNotFoundError:
        st.warning(f"Gráfico {plot_name} não encontrado")

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def show_image_with_download(img_path, caption):
    try:
        st.image(img_path, caption=caption)
        with open(img_path, 'rb') as f:
            st.download_button(
                label=f"⬇️ Baixar {caption}",
                data=f,
                file_name=f"{caption}.png",
                mime="image/png",
                on_click="ignore"
            )
                
        os.remove(img_path)
    except FileNotFoundError:
        st.error(f"Arquivo de imagem não encontrado: {img_path}")
    except Exception as e:
        st.error(f"Erro ao exibir imagem: {str(e)}")

# Função de avaliação completa com pipeline e botões
def full_evaluation(model):
    st.markdown("---")
    st.header("Avaliação Completa do Modelo")

    # Pipeline do Modelo no topo
    with st.expander(":wrench: Pipeline do Modelo", expanded=False):
        pipeline = exp.pipeline
        st.write(pipeline)
        st.markdown("---")

    # Linha 1: Métricas principais
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("📈 Curva AUC-ROC", expanded=False):
            plot_model(model, plot='auc', save=True, verbose=False)
            show_image_with_download('AUC.png', 'Curva AUC-ROC')

        with st.expander("🧮 Matriz de Confusão", expanded=False):
            plot_model(model, plot='confusion_matrix', save=True, verbose=False)
            show_image_with_download('Confusion Matrix.png', 'Matriz de Confusão')

    with col2:
        with st.expander("📉 Curva Precision-Recall", expanded=False):
            plot_model(model, plot='pr', save=True, verbose=False)
            show_image_with_download('Precision Recall.png', 'Curva Precision-Recall')

        with st.expander("📋 Relatório de Classificação", expanded=False):
            plot_model(model, plot='class_report', save=True, verbose=False)
            show_image_with_download('Class Report.png', 'Relatório de Classificação')

    
    # Linha 2: Análise detalhada
    col3, col4 = st.columns(2)
    with col3:
        with st.expander("🔍 Importância das Variáveis", expanded=False):
            plot_model(model, plot='feature', save=True, verbose=False)
            show_image_with_download('Feature Importance.png', 'Importância das Variáveis')
        
        with st.expander("🎚️ Análise de Limiar", expanded=False):
            plot_model(model, plot='threshold', save=True, verbose=False)
            st.image('Threshold.png')
            save_plot('Threshold')
            os.remove('Threshold.png')

            
    
    with col4:
        with st.expander("📊 Erro de Predição", expanded=False):
            plot_model(model, plot='error', save=True, verbose=False)
            show_image_with_download('Prediction Error.png', 'Erro de Predição')

        with st.expander("⚖️ Curva de Calibração", expanded=False):
            plot_model(model, plot='calibration', save=True, verbose=False)
            show_image_with_download('Calibration Curve.png', 'Curva de Calibração')




# Lógica principal do aplicativo
if uploaded_file is not None or 'sample_data' in st.session_state:
    if run_button:
        with st.spinner('Processando dados e treinando modelo...'):
            try:
                # Carregamento dos dados
                if uploaded_file.name.endswith('.ftr'):
                    df = pd.read_feather(uploaded_file)
                else:
                    df = pd.read_pickle(uploaded_file)
                
                # Tratamento da amostra
                if 'sample_data' not in st.session_state:
                    df_sample = df.sample(frac=0.2, random_state=27)
                    st.session_state.sample_data = df_sample
                
                df = st.session_state.sample_data if use_sample else df
                df = df.drop(columns='index', errors='ignore')
                
                # Divisão por data
                data_maxima = df['data_ref'].max()
                df_base = df[df['data_ref'] <= (data_maxima - pd.DateOffset(months=3))]
                
                # Processamento de categorias
                cat_cols = ['sexo', 'posse_de_veiculo', 'posse_de_imovel', 
                           'tipo_renda', 'educacao', 'estado_civil', 'tipo_residencia']
                for col in cat_cols:
                    freq = df_base[col].value_counts(normalize=True)
                    rare_cats = freq[freq < threshold].index
                    df_base[col] = df_base[col].replace(rare_cats, 'outros')

                # Configuração do PyCaret com correção
                import pycaret.classification
                pycaret.classification._CURRENT_EXPERIMENT = None
                
                with tempfile.TemporaryDirectory() as tmp_dir:
                    # Setup
                    exp = setup(
                        data=df_base,
                        target='mau',
                        train_size=train_size,
                        session_id=123,
                        categorical_features=cat_cols,
                        numeric_features=[c for c in df_base.select_dtypes(include=['number']).columns if c != 'mau'],
                        normalize=True,
                        log_experiment=False,
                        ignore_features=['data_ref'],
                        fix_imbalance=True
                    )
                    
                    st.success("Configuração concluída!")
                    with st.expander("Configuração do Setup", expanded=False):
                        setup_df = pull()
                        st.dataframe(setup_df)
                    
                    with st.expander("Comparação de Modelos", expanded=False):
                        with st.spinner('Comparando modelos...'):
                            best_model = compare_models(verbose=False)
                            compare_df = pull()
                            st.dataframe(compare_df)
                    
                    with st.spinner('Treinando LightGBM...'):
                        lightgbm_model = create_model('lightgbm', verbose=False)
                        tuned_lightgbm = tune_model(lightgbm_model, verbose=False)
                    
                    full_evaluation(tuned_lightgbm)
                    
                    # Salvamento do modelo
                    model_path = os.path.join(tmp_dir, 'model')
                    save_model(tuned_lightgbm, model_path)
                    
                    
                    with open(f"{model_path}.pkl", 'rb') as f:
                        st.download_button(
                            label="💾 Baixar Modelo Treinado",
                            data=f,
                            file_name="modelo_credit_scoring.pkl",
                            help="Salve o modelo LightGBM treinado no seu computador",
                            on_click="ignore"
                        )
                
                st.balloons()
                
            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")
else:
    st.info("👈 Por favor, carregue um dataset para começar")