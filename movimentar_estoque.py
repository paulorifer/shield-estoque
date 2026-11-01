import sqlite3

def movimentar_peca(sku, qtd_movimento, operacao):
    # 1. Conecta ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    
    # Garante que as chaves estrangeiras estão ativas
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        # 2. Localiza o produto pelo SKU para descobrir o seu ID, o saldo atual e a descrição
        cursor.execute("""
            SELECT l.id_estoque, l.quantidade, p.descricao, p.id_produto
            FROM tb_estoque_localizacao l
            JOIN tb_produtos p ON l.id_produto = p.id_produto
            WHERE p.codigo_sku = ?
        """, (sku,))
        
        resultado = cursor.fetchone()
        
        if not resultado:
            print(f"Erro: O produto com SKU '{sku}' não foi encontrado no estoque!")
            return

        id_estoque, quantidade_atual, descricao, id_produto = resultado

        # 3. Calcula o novo saldo dependendo se é ENTRADA (soma) ou SAIDA (subtrai)
        if operacao.upper() == 'ENTRADA':
            nova_quantidade = quantidade_atual + qtd_movimento
        elif operacao.upper() == 'SAIDA':
            if quantidade_atual < qtd_movimento:
                print(f"Erro: Estoque insuficiente! Saldo atual: {quantidade_atual}, Tentativa de retirada: {qtd_movimento}")
                return
            nova_quantidade = quantidade_atual - qtd_movimento
        else:
            print("Erro: Operação inválida! Use 'ENTRADA' ou 'SAIDA'.")
            return

        # 4. Atualiza a tabela de estoque com a nova quantidade real
        cursor.execute("""
            UPDATE tb_estoque_localizacao
            SET quantidade = ?
            WHERE id_estoque = ?
        """, (nova_quantidade, id_estoque))

        # 5. Insere o registo na tabela de auditoria (Histórico)
        cursor.execute("""
            INSERT INTO tb_historico_movimentacao 
            (id_produto, quantidade, quantidade_anterior, quantidade_atual, motivo)
            VALUES (?, ?, ?, ?, ?)
        """, (id_produto, qtd_movimento, quantidade_atual, nova_quantidade, operacao.upper()))

        # 6. Salva (commit) todas as alterações no banco de dados com segurança
        conn.commit()
        print(f"Sucesso! Movimentação de {operacao.upper()} realizada para o produto: {descricao}")
        print(f"Saldo anterior: {quantidade_atual} | Novo saldo: {nova_quantidade} unidades.")
        print(f"Histórico de auditoria registado com sucesso!")

    except Exception as e:
        # Se der algum erro, desfaz qualquer alteração para proteger os dados
        conn.rollback()
        print(f"Erro crítico durante a movimentação: {e}")
        
    finally:
        # Fecha sempre a conexão
        conn.close()

# Testando a movimentação: Retirar 5 unidades do amortecedor (SKU-AMOR-01)
if __name__ == "__main__":
    print("A processar movimentação de estoque com auditoria...")
    movimentar_peca(sku="SKU-AMOR-01", qtd_movimento=2, operacao="SAIDA")