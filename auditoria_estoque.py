import sqlite3

def conectar():
    """Abre a conexão com o banco de dados do Shield Estoque."""
    return sqlite3.connect('banco.db')

def cadastrar_localizazione():
    """Ajuda a organizar onde a peça deve ficar guardada para evitar sumiços."""
    print("\n--- CADASTRO DE LOCALIZAÇÃO DE PEÇA ---")
    codigo = input("Digite o código de barras da peça: ")
    nome = input("Nome da peça: ")
    local = input("Onde ela fica guardada? (Ex: Prateleira B, Caixa 3): ")
    quantidade_inicial = int(input("Quantidade atual no estoque físico: "))

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO pecas (codigo_barras, nome, quantidade, localizacao)
            VALUES (?, ?, ?, ?)
        """, (codigo, nome, quantidade_inicial, local))
        
        conexao.commit()
        print("✅ Peça cadastrada e localização salva com sucesso!")
    except sqlite3.IntegrityError:
        print("⚠️ Erro: Esse código de barras já está cadastrado no sistema.")
    finally:
        conexao.close()

def conferir_divergencia():
    """
    Ferramenta principal para achar a peça fantasma: 
    Compara o que está no sistema com o que você contou fisicamente.
    """
    print("\n--- AUDITORIA RÁPIDA (LOCALIZAR PEÇA FANTASMA) ---")
    codigo = input("Digite o código de barras da peça que vai conferir: ")

    conexao = conectar()
    cursor = conexao.cursor()

    # Busca a peça no banco
    cursor.execute("SELECT id, nome, quantidade, localizacao FROM pecas WHERE codigo_barras = ?", (codigo,))
    peca = cursor.fetchone()

    if peca:
        id_peca, nome, qtd_sistema, local = peca
        print(f"\n📦 Peça encontrada: {nome}")
        print(f"📍 Localização esperada: {local}")
        print(f"💻 Quantidade registrada no sistema: {qtd_sistema}")

        qtd_fisica = int(input("🔢 Digite o número de peças que VOCÊ CONTOU fisicamente na prateleira: "))

        # Calcula a divergência
        diferenca = qtd_fisica - qtd_sistema

        if diferenca == 0:
            print("✅ Estoque batido! Nenhuma divergência encontrada.")
        elif diferenca < 0:
            print(f"🚨 ALERTA DE PEÇA FANTASMA! O sistema tem a mais. Estão faltando {abs(diferenca)} unidades!")
        else:
            print(f"⚠️ Atenção: Há {diferenca} unidades a mais fisicamente do que no sistema.")

        # Pergunta se quer atualizar o sistema com o valor real contado
        atualizar = input("Deseja atualizar o sistema com o valor contado? (s/n): ").strip().lower()
        if atualizar == 's':
            cursor.execute("UPDATE pecas SET quantidade = ? WHERE id = ?", (qtd_fisica, id_peca))
            conexao.commit()
            print("🔄 Sistema atualizado com a contagem física real!")
    else:
        print("❌ Peça não encontrada no banco de dados. Cadastre-a primeiro.")

    conexao.close()

# Menu principal simples
if __name__ == '__main__':
    while True:
        print("\n=== SHIELD ESTOQUE - CONTROLE DE DIVERGÊNCIA ===")
        print("1. Cadastrar nova peça e localização")
        print("2. Fazer auditoria rápida (Conferir peça fantasma)")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == '1':
            cadastrar_localizazione()
        elif opcao == '2':
            conferir_divergencia()
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")