
# TaskFlow API

API REST para gerenciamento de tarefas, desenvolvida com Python, FastAPI, SQLAlchemy e SQLite.

Projeto pessoal de aprendizado em desenvolvimento backend.

## Tecnologias

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefas por ID
- Atualizar tarefas parcialmente
- Excluir tarefas
- Persistir dados em SQLite
- Validar dados e tratar erros HTTP

## Estrutura do projeto

- `app/main.py`: inicialização da aplicação
- `app/database.py`: configuração do banco
- `app/models.py`: modelos SQLAlchemy
- `app/schemas.py`: schemas Pydantic
- `app/routers/tasks.py`: endpoints de tarefas
- `tests/`: testes automatizados (planejados)

## Como executar

Crie e ative um ambiente virtual Python.

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Verificar a API |
| POST | /tasks | Criar tarefa |
| GET | /tasks | Listar tarefas |
| GET | /tasks/{task_id} | Consultar tarefa |
| PATCH | /tasks/{task_id} | Atualizar tarefa |
| DELETE | /tasks/{task_id} | Excluir tarefa |

## Banco de dados

A aplicação utiliza SQLite para persistir as tarefas.

O arquivo `taskflow.db` é criado automaticamente na inicialização da aplicação e não deve ser versionado no Git.

## Próximas melhorias

- Testes automatizados com pytest
- Docker
- CI/CD
- Migrações de banco com Alembic
