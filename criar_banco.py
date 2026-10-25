import sqlite3

# 1. Conecta (ou cria se não existir) o arquivo do banco de dados
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# 2. Lê o conteúdo do arquivo schema.sql
with open('schema.sql', 'r', encoding='utf-8') as arquivo_sql:
    script_sql = arquivo_sql.read()

# 3. Executa todo o script SQL para criar as tabelas
cursor.executescript(script_sql)

# 4. Salva as alterações e fecha a conexão
conn.commit()
conn.close()

print("Sucesso! O banco de dados 'estoque.db' e as tabelas foram criados com sucesso!")