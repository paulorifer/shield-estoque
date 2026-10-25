import sqlite3

# 1. Conecta ao nosso banco de dados existente
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Garante que as chaves estrangeiras estão ativas
cursor.execute("PRAGMA foreign_keys = ON;")

# 2. Cadastra um produto novo (SKU, Descrição e Categoria)
cursor.execute("""
    INSERT INTO tb_produtos (codigo_sku, descricao, categoria)
    VALUES (?, ?, ?)
""", ("SKU-AMOR-01", "Amortecedor Dianteiro", "Suspensão"))

# Pega o ID do produto que acabou de ser criado
id_produto_criado = cursor.lastrowid

# 3. Cadastra o sub-endereço exato (A cura da peça fantasma: Prédio, Prateleira, Gaveta)
cursor.execute("""
    INSERT INTO tb_sub_enderecos (predio, prateleira, gaveta)
    VALUES (?, ?, ?)
""", ("Rua A", "Prateleira 03", "Gaveta B2"))

# Pega o ID do endereço que acabou de ser criado
id_endereco_criado = cursor.lastrowid

# 4. Vincula o produto ao sub-endereço com uma quantidade no estoque real
cursor.execute("""
    INSERT INTO tb_estoque_localizacao (id_produto, id_sub_endereco, quantidade)
    VALUES (?, ?, ?)
""", (id_produto_criado, id_endereco_criado, 15))

# 5. Salva (commit) as alterações no banco e fecha a conexão
conn.commit()
conn.close()

print("Sucesso! Produto cadastrado e posicionado na Gaveta B2 com 15 unidades!")