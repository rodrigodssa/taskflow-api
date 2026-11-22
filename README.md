
# TaskFlow API

API REST de gerenciamento de tarefas desenvolvida com Python e FastAPI.

## Tecnologias

- Python
- FastAPI
- Pydantic
- Uvicorn

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefas por ID
- Atualizar tarefas
- Excluir tarefas
- Validação de dados e tratamento de erros HTTP

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
python -m uvicorn main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

## Observações

Projeto de aprendizado em desenvolvimento backend.

Atualmente, as tarefas são armazenadas em memória e são perdidas ao reiniciar o servidor.

## Próximos passos

- Banco de dados SQL
- Testes automatizados
- Docker
