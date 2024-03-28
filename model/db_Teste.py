from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import time
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a string de conexão do PostgreSQL do arquivo .env
CONN_POSTGRESQL = os.getenv('CONN_POSTGRESQL')

# Criar a conexão com o banco de dados
engine = create_engine(CONN_POSTGRESQL)

# Criar uma sessão a partir do engine
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Chamar a stored procedure 'spr_taskmanager_0001' com um parâmetro _ID_Guid
    #sql_query = text('SELECT ds_log FROM "db_DxCorp_Servicos".tbl_log;')
    sql_query = text('CALL "db_DxCorp_Servicos".spr_taskmanager_0001(:_ID_Guid)')
    
    result = session.execute(sql_query, {'_ID_Guid': 'eca4a6ad-3261-402d-b265-eacc432f3876'})

    # Recuperar o resultado, se necessário
    rows = result.fetchall()
    print(rows)

    
    result = session.execute(sql_query)

    # Recuperar o resultado, se necessário
    rows = result.fetchall()
    print(rows)

except Exception as e:
    print("Erro ao executar a stored procedure:", e)

finally:
    # Adicionar um atraso de 5 segundos antes de fechar a sessão
    time.sleep(5)

    # Fechar a sessão
    session.close()
