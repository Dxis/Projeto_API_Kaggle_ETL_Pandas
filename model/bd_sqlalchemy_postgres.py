from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
import os
from dotenv import load_dotenv
import uuid
import time  # Importe o módulo time
from sqlalchemy import text

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a string de conexão do PostgreSQL do arquivo .env
CONN_POSTGRESQL = os.getenv('CONN_POSTGRESQL')

# Crie a conexão com o banco de dados
engine = create_engine(CONN_POSTGRESQL)

def Db_Postgres_truncateSpotify():
    # SQL para chamar a stored procedure com o GUID fixo
    sql_query = text(f'')

    with engine.connect() as conn:

        # Execute a consulta SQL
        sql_query = text(f'truncate table "db_DxCorp_Servicos".tbl_log;')
        result = conn.execution_options(stream_results=True).execute((sql_query))
  
           
def Db_Postgres_Sel_log():
    # Gerar um UUID fixo para pesquisa
    _ID_Guid = 'eca4a6ad-3261-402d-b265-eacc432f3876'

    # SQL para chamar a stored procedure com o GUID fixo
    sql_query = text(f'SELECT ds_log FROM "db_DxCorp_Servicos".tbl_log WHERE ID_GUID = :_ID_Guid')

    print(sql_query, {'_ID_Guid': _ID_Guid})

    with engine.connect() as conn:
        # Execute a consulta SQL
            # Execute a consulta SQL
        #result = conn.execution_options(stream_results=True).execute(text("select * from public.tblstage_spotify;"))
        #result = conn.execution_options(stream_results=True).execute(text('select * from "db_DxCorp_Servicos".tblSpotify;'))
        result = conn.execution_options(stream_results=True).execute((sql_query))
        # Execute a consulta SQL
        #result = conn.execute(sql_query, {'_ID_Guid': _ID_Guid})

        # Iterar sobre os resultados e imprimir cada linha
        for row in result:
            print(row)


if __name__ == "__main__":
    #Db_MySQL_Sel_log()
    #Db_MySQL_Sel_log()
    Db_Postgres_truncateSpotify()   
