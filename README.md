# 🛡️ Shield Estoque

## 📖 História & Motivação
Trabalhando no estoque, não tem nada pior do que o sistema garantir que a peça está lá, você ir no endereço físico e... nada. O item sumiu. Foi exatamente por causa dessa dor de cabeça e das famosas "peças fantasmas" que criei o **Shield Estoque**. A ideia é ter uma ferramenta rápida em Python e SQLite para verificar o inventário, bater os dados e achar onde está o furo antes que isso vire um problema na hora de separar o pedido.

## 💡 O que é o projeto hoje?
Hoje ele é um sistema pequeno de auditoria que criei para treinar modelagem de banco de dados relacional, testar consultas SQL na prática e colocar mais um projeto forte no meu portfólio de backend.

## 🛠️ Decisões Técnicas
- **Python:** Escolhi porque é a linguagem que uso para automatizar meus estudos e facilita muito na hora de montar a lógica.

- **SQLite & SQL:** Aqui eu quis sair do arquivo JSON simples e ir para um banco relacional de verdade. Queria aprender na prática como criar tabelas, chaves e fazer consultas cruzadas (`SELECT`, `JOIN`) já que tambem ta fazendo parte dos meus estudos da universidade.


## 📂 Estrutura do Projeto
- `schema.sql`: O arquivo que cria a estrutura e as tabelas do banco de dados do zero.

- `main.py`: O script principal que conecta no banco, roda as consultas e faz a mágica acontecer.

- `banco.db`: O arquivo local onde o SQLite guarda tudo de forma leve.


## 🚀 Como Executar
1. Tenha o **Python 3** instalado no seu computador.

2. Baixe ou clone este repositório.
3. Abra a pasta no VS Code.
4. Rode o comando no terminal: `python main.py`

## 🧠 Aprendizados e dificuldades
Confesso que apanhar de conexão com banco de dados, fechar direito as sessões e estruturar o `schema.sql` no começo foi trabalhoso. Tive que quebrar a cabeça para garantir que o script não corrompesse os dados. Mas passar por isso me fez perceber sobre como funciona o backend por trás de um sistema e que se for estruturado de forma errada, ele quebra e eu perco parte do projeto.

## ⚠️ Limitações e Próximos Passos
Como ele roda direto no terminal e foca em consultas pontuais, ele resolve bem o problema de estudo e auditoria rápida, mas ainda é simples.
- **Onde quero chegar:** O próximo passo é criar scripts que gerem relatórios automáticos de divergências e deixar o tratamento de erros mais visiveis para auxiliar na correção deles.