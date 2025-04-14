import sqlite3

# Conectando ao banco
conn = sqlite3.connect("carrinho.db")
cursor = conn.cursor()

# Descobrindo as tabelas (opcional)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()
print("Tabelas disponíveis no banco:")
for tabela in tabelas:
    print(f" - {tabela[0]}")

# Consultando os dados (ajuste o nome da tabela se necessário)
print("\nConteúdo da tabela 'produtos':")
try:
    cursor.execute("SELECT * FROM produtos;")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
except Exception as e:
    print("Erro ao consultar a tabela:", e)

conn.close()
