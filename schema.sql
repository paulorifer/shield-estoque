-- Habilita o suporte a chaves estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- 1. TABELA DE PRODUTOS / PEÇAS
CREATE TABLE IF NOT EXISTS tb_produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_sku VARCHAR(50) UNIQUE NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    categoria VARCHAR(30)
);

-- 2. TABELA DE ESTRUTURA DE SUB-ENDEREÇO (A cura da Peça Fantasma)
CREATE TABLE IF NOT EXISTS tb_sub_enderecos (
    id_sub_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
    predio VARCHAR(10) NOT NULL,      -- Ex: Rua A, Corredor 01
    prateleira VARCHAR(10) NOT NULL,  -- Ex: Prateleira 03
    gaveta VARCHAR(10) NOT NULL,      -- Ex: Gaveta B2 (Sub-endereço)
    status_endereco VARCHAR(20) DEFAULT 'DISPONIVEL'
);

-- 3. TABELA DE SALDO REAL POR SUB-ENDEREÇO
CREATE TABLE IF NOT EXISTS tb_estoque_localizacao (
    id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    id_sub_endereco INTEGER NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade >= 0),
    FOREIGN KEY (id_produto) REFERENCES tb_produtos(id_produto),
    FOREIGN KEY (id_sub_endereco) REFERENCES tb_sub_enderecos(id_sub_endereco)
);

-- 4. TABELA DE AUDITORIA DE MOVIMENTAÇÃO (Rastreio total de quem/onde moveu)
CREATE TABLE IF NOT EXISTS tb_historico_movimentacao (
    id_movimentacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    id_origem INTEGER,         -- De onde a peça saiu (id_sub_endereco)
    id_destino INTEGER,        -- Para onde a peça foi (id_sub_endereco)
    quantidade INT NOT NULL,
    motivo VARCHAR(50) NOT NULL, -- Ex: 'TRANSFERENCIA', 'AUDITORIA_FANTASMA', 'AJUSTE'
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_produto) REFERENCES tb_produtos(id_produto)
);