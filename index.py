import pandas as pd
from pandasql import sqldf
from dotenv import load_dotenv
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from sqlalchemy import create_engine


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Autenticação Kaggle e download do insumo
def baixar_Arq_Kaggle(DataSet_Kaggle):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset=DataSet_Kaggle, path="./", unzip=True)

# Etl com Pandas e pandasql
def ETL_Pandas(caminho_arquivo):
    # Carregar o arquivo CSV usando o Pandas
    df = pd.read_csv(caminho_arquivo, delimiter=',')

    # Definir a consulta SQL que você deseja executar
    consulta_sql = """
        SELECT count(0) as qtde,
               artist_names,
               sum(tempo) as tempo
        FROM df 
        GROUP BY artist_names
        ORDER BY tempo DESC 
        LIMIT 5 
    """

    # Executar a consulta SQL no DataFrame
    resultado = sqldf(consulta_sql)

    # Armazenar o resultado em um novo DataFrame
    df_top5 = pd.DataFrame(resultado)

    # Criar uma conexão SQLAlchemy
    if var == 1:
        print("CONN_POSTGRESQL:", CONN_POSTGRESQL)      
        ConectarBanco(CONN_POSTGRESQL, df, df_top5)         
    if var == 2:
        print("CONN_MYSQL:", CONN_MYSQL)
        ConectarBanco(CONN_MYSQL, df, df_top5)
       

# Conectar ao banco de dados e inserir dados
def ConectarBanco(CONN_STRING, df, df_top5):
    
    # Criar uma conexão SQLAlchemy
    
    engine = create_engine(CONN_STRING)    

    tblspotify_topsongs = 'tblspotify_topsongs'
    df.to_sql(tblspotify_topsongs, engine, if_exists='replace', index=False)

    tblTop5_Spotify = 'tbltop5_spotify'
    df_top5.to_sql(tblTop5_Spotify, engine, if_exists='replace', index=False)

if __name__ == "__main__":
    # Acessar as variáveis de ambiente carregadas
    Arquivo = os.getenv('ARQUIVO')
    DataSet_Kaggle = os.getenv('DATASET_KAGGLE')
    Stage = os.getenv('Stage')
    CONN_POSTGRESQL = os.getenv('CONN_POSTGRESQL')
    CONN_MYSQL = os.getenv('CONN_MYSQL')
    var = int(os.getenv('VAR'))

    caminho_arquivo = Stage + "\\" + Arquivo  # Caminho para o arquivo CSV

    # Verificar se o arquivo já existe no diretório
    if not os.path.exists(caminho_arquivo):
        baixar_Arq_Kaggle(caminho_arquivo, DataSet_Kaggle)

    ETL_Pandas(caminho_arquivo)
