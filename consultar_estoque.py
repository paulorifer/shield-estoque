import sqlite3

# 1. Conecta ao nosso banco de dados
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# 2. Faz a consulta unindo a tabela de estoque, produtos e sub-endereços
cursor.execute("""
    SELECT p.codigo_sku, p.descricao, e.predio, e.prateleira, e.gaveta, l.quantidade
    FROM tb_estoque_localizacao l
    JOIN tb_produtos p ON l.id_produto = p.id_produto
    JOIN tb_sub_enderecos e ON l.id_sub_endereco = e.id_sub_endereco
""")

# Pega todos os resultados encontrados
resultados = cursor.fetchall()

# 3. Exibe os dados de forma limpa no terminal
print("\n" + "="*40)
print("     RELATÓRIO DE ESTOQUE - SHIELD ESTOQUE")
print("="*40)

for linha in resultados:
    sku, descricao, predio, prateleira, gaveta, quantidade = linha
    print(f"📦 SKU: {sku} - {descricao}")
    print(f"📍 Localização: {predio} > {prateleira} > {gaveta}")
    print(f"📊 Quantidade Real: {quantidade} unidades")
    print("-" * 40)

# Fecha a conexão com o banco
conn.close()