-- Estrutura inicial do banco de dados para o Shield Estoque

CREATE TABLE IF NOT EXISTS pecas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_barras TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 0,
    localizacao TEXT
);