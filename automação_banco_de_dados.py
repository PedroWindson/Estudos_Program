# Importa a biblioteca necessária para se conectar ao banco de dados MySQL
import mysql.connector
from mysql.connector import Error
import time  # Importa a biblioteca para controlar o tempo

# Configurações de conexão com o banco de dados
db_config = {
    'host': '111.111.111.111',        # O endereço do servidor onde o banco de dados está hospedado
    'user': 'user_root',          # O nome do usuário com permissões para acessar o banco
    'password': 'password',   # A senha do usuário para autenticação
    'database': 'db_name'     # O nome do banco de dados em que você quer realizar a operação
}

# Função para executar o código de atualização no banco
def executar_query():
    try:
        # Tentando se conectar ao banco de dados com as configurações fornecidas
        connection = mysql.connector.connect(**db_config)

        # Verifica se a conexão foi bem-sucedida
        if connection.is_connected():
            print("Conectado ao banco de dados")

            # Cria um cursor para executar comandos SQL no banco de dados
            cursor = connection.cursor()

            # Define o comando SQL que queremos executar
            sql_query = """
            UPDATE faturamento AS f
            INNER JOIN faturamento_pagamento AS fp ON fp.id_faturamento = f.id_faturamento
            SET f.databaixa = fp.data
            WHERE fp.id_tipopagamento = 0 AND f.databaixa IS NULL AND fp.valor > 0;
            """

            # Executa a consulta SQL no banco de dados
            cursor.execute(sql_query)

            # Comita as mudanças, ou seja, confirma a execução do UPDATE no banco de dados
            connection.commit()

            # Exibe o número de linhas que foram alteradas pelo comando SQL
            print(f"{cursor.rowcount} linhas atualizadas.")
    
    except Error as e:
        print(f"Erro ao conectar ou executar a consulta: {e}") # Exibe uma mensagem de erro, caso a conexão ou a execução da consulta falhem

    finally:
        # Esse bloco é sempre executado, independente de ter ocorrido erro ou não
        if connection.is_connected(): # Verifica se a conexão com o banco de dados está aberta
            
            cursor.close() # Fecha o cursor (o que estava executando os comandos SQL)
            
            connection.close() # Fecha a conexão com o banco de dados
            print("Conexão encerrada.")

# Loop para executar a função a cada 30 minutos
while True:
    executar_query()  # Executa a função de consulta
    time.sleep(30 * 60)  # Espera por 30 minutos (30 * 60 segundos)
