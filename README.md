# 🛍️ Carrinho de Compras - Backend API

Projeto como requisito para Pós Graduação em Desenvolvimento FullStack PucRio, para Desenvolvimento Back-End Avançado.Este projeto consiste em uma **API REST** desenvolvida com **FastAPI** para gerenciar produtos em um carrinho de compras virtual. Os dados são persistidos em um banco de dados **SQLite**, permitindo operações de **criação**, **leitura**, **atualização** e **remoção** de produtos.

## 🚀 Funcionalidades

- ✅ Adicionar produtos ao carrinho (`POST /produtos`)
- 📄 Listar produtos (`GET /produtos`)
- ✏️ Atualizar informações de um produto (`PUT /produtos/{id}`)
- ❌ Remover produto do carrinho (`DELETE /produtos/{id}`)
- 🔎 Documentação automática com Swagger UI

---

## 🛠️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/DanilloAlve/Carrinho-ActiveStyle_API_Backend

```

### 2. Crie e ative um ambiente virtual

```bash
# Criação do ambiente virtual
python -m venv venv

# Ativação
venv\Scripts\activate

```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a aplicação

```bash
uvicorn main:app --reload
```


---

## 🌐 Acessando a API

Após iniciar o servidor, acesse:

- Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)


---



---
## 🐳 Executando com Docker

### Pré-requisitos

- **Docker** (>= 20.10.0)
- **Docker Compose** (>= 1.29.0)

### Passos para execução

1. **Construa e inicie o container**:
   No diretório raiz do projeto, execute:
   ```bash
   docker-compose up --build
   ```

2. **Acesse a API**:
   - Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)


---

## 👨‍💻 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [Docker](https://www.docker.com/)

---
