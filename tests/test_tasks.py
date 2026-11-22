
def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Estudar FastAPI",
            "description": "Criar testes automatizados",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Estudar FastAPI"
    assert data["completed"] is False


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Primeira tarefa"})
    client.post("/tasks", json={"title": "Segunda tarefa"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_task(client):
    created = client.post(
        "/tasks", json={"title": "Estudar SQLAlchemy"}
    ).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Estudar SQLAlchemy"


def test_get_task_not_found(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_update_task(client):
    created = client.post(
        "/tasks", json={"title": "Estudar Python"}
    ).json()

    response = client.patch(
        f"/tasks/{created['id']}",
        json={"completed": True},
    )

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task(client):
    created = client.post(
        "/tasks", json={"title": "Tarefa temporária"}
    ).json()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 204
    assert client.get(f"/tasks/{created['id']}").status_code == 404


def test_create_task_without_title(client):
    response = client.post(
        "/tasks",
        json={"description": "Sem título"},
    )

    assert response.status_code == 422
