from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

#Definindo o titulo da página e o icone da aba.
st.set_page_config(page_title="NOGD3V", page_icon=":globe_with_meridians:", layout="wide")

#Função para acessar a animação.

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Usar CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#BARRA DE NAVEGAÇÃO LATERAL
EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Menu",
                options=["Home", "Projects", "Contact"],
                icons=["house", "book", "envelope"],
                menu_icon="cast",
                default_index=0,
            )
        return selected

selected = streamlit_menu(example=EXAMPLE_NO)


#HEADER
with st.container():
    st.subheader("Olá, me chamo Lucas :wave:")
    st.title("O melhor engenheiro de dados do meu bairro :infinity:")
    st.write("##")
    st.write("Apaixonado pela área de dados, extraio, carrego e transformo dados para solucionar problemas empresáriais.")
    st.write("[Visite meu LINKEDIN > ](https://www.linkedin.com/in/nogd3v/)")



#Importando assets

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_dews3j6m.json")
img_contact_form = Image.open("images/api.png")
img_lottie_animation = Image.open("images/request_api.png")


#Sessão: Dia a dia

with st.container():
    st.write("---") #adiciona uma linha divisória entre as sessões.
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Meu dia a dia (tools)")
        st.write("##")
        st.write(
            """
            Atualmente essas são as minhas competencias para solucionar problemas:

            Competências: iceberg · Integração e entrega contínuas (CI/CD) · Minio · Trino · Kubernetes · Apache Airflow · Bitbucket · ETL (Extração, transformação e carregamento) · Tunning · Administrador de banco de dados · Monitoramento de banco de dados · Python · Google Cloud Platform (GCP) · PostgreSQL · Apache Spark · PySpark · Microsoft SQL Server · SSIS · SQL · Transact-SQL · Docker · Linux · Scrum

            """
        )


    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

#Sessão: Pojetos

with st.container():
    st.write("---")
    st.header("PROJETOS :compass:")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("CRUD com PYTHON e FLASK")
        st.write(

            """
            Nesta api usamos python com o framework flask para criar uma API que cria, lê, atualiza e exclui (CRUD) livros.

            Foi utilizado o localhost e o postman para verificar a funcionalidade
            """
        )
        st.markdown("[VEJA >](https://github.com/nogD3V/simplePythonFlaskApi)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Consumindo api com python")
        st.write(

            """
            Neste app utilizamos PYTHON com o framework REQUESTS para solicitar dados da API do github e STREAMLIT para criar uma interface que foi estilizada com BOOTSTRAP e CSS .
            """
        )
        st.markdown("[VEJA >](https://github.com/nogD3V/requestApi)")

with st.container():
    st.write("---")
    st.header("Entre em contato!")
    st.write("##")

    #Formulario
    contact_form = """
    <form action="https://formsubmit.co/lucas.nsilva033@gmail.com" method="POST">
     <input type="hidden" name ="_captcha" value="false">
     <input type="text" name="name" placeholder="Seu nome" required>
     <input type="email" name="email" placeholder="Seu email" required>
     <textarea name ="Mensagem" placeholder="Deixe sua mensagem" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()