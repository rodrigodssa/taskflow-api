# TaskFlow API

API REST para gerenciamento de tarefas, desenvolvida com Python, FastAPI, SQLAlchemy e SQLite.

Projeto pessoal de aprendizado em desenvolvimento backend, com foco em organização de código, persistência de dados, testes automatizados e conteinerização.

## Tecnologias

- Python 3.13
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn
- Pytest
- HTTPX
- Docker e Docker Compose

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefas por ID
- Atualizar tarefas parcialmente
- Excluir tarefas
- Persistir dados em SQLite
- Validar dados e tratar erros HTTP
- Executar testes automatizados
- Executar a API com Docker e volume persistente

## Estrutura do projeto

```text
TaskFlow_API/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       └── tasks.py
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar localmente

Requisitos: Python 3.13 e pip.

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação interativa:

http://localhost:8000/docs

## Como executar com Docker

Requisitos: Docker e Docker Compose.

Na raiz do projeto, execute:

```bash
docker compose up --build -d
```

Acesse a documentação interativa:

http://localhost:8000/docs

Verifique o status do contêiner:

```bash
docker compose ps
```

Para acompanhar os logs:

```bash
docker compose logs -f api
```

Para parar e remover o contêiner:

```bash
docker compose down
```

O volume Docker é preservado ao executar `docker compose down`.

**Atenção:** o comando `docker compose down -v` também remove o volume, apagando os dados armazenados nele.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Verificar a API |
| POST | /tasks | Criar tarefa |
| GET | /tasks | Listar tarefas |
| GET | /tasks/{task_id} | Consultar tarefa |
| PATCH | /tasks/{task_id} | Atualizar tarefa |
| DELETE | /tasks/{task_id} | Excluir tarefa |

### Exemplo de criação de tarefa

**POST `/tasks`**

```json
{
  "title": "Estudar FastAPI",
  "description": "Praticar desenvolvimento backend"
}
```

Resposta esperada: HTTP `201 Created`.

```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Praticar desenvolvimento backend",
  "completed": false
}
```

O ID retornado depende dos registros existentes no banco.

### Exemplo de atualização

**PATCH `/tasks/1`**

```json
{
  "completed": true
}
```

## Banco de dados

A aplicação utiliza SQLite com SQLAlchemy.

**Execução local:** o banco é armazenado no arquivo `taskflow.db`, criado automaticamente na raiz do projeto.

**Execução com Docker:** o banco é armazenado em `/data/taskflow.db`, dentro de um volume Docker persistente.

A configuração pode ser alterada por meio da variável de ambiente `DATABASE_URL`.

O arquivo local `taskflow.db` não é versionado no Git.

## Testes automatizados

O projeto possui testes automatizados com Pytest para os principais fluxos do CRUD e validações HTTP.

Para executar:

```bash
python -m pytest -v
```

Os testes utilizam um banco SQLite separado em memória, evitando alterações nos dados da aplicação.

## Próximas melhorias

- CI/CD com GitHub Actions
- Migrações de banco com Alembic
- Autenticação e autorização
- Paginação e filtros na listagem de tarefas
