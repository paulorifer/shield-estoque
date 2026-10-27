import sqlite3

def inicializar_banco():
   # 1. Conecta (ou cria) o arquivo do banco de dados na mesma pasta
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # 2. Abre e lê o arquivo schema.sql que criei
    with open('schema.sql', 'r', encoding='utf-8') as arquivo_sql:
        script_sql = arquivo_sql.read()

    # 3. Executa todo o comando SQL dentro do arquivo
    cursor.executescript(script_sql)

    # 4. Salva as alterações e fecha a conexão com segurança
    conexao.commit()
    conexao.close()
    print("✅ Banco de dados do Shield Estoque inicializado com sucesso!")

# Ponto de partida do programa
if __name__ == '__main__':
    inicializar_banco()