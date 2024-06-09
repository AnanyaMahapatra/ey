from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_addition_success():
    response = client.post("/add", json={ "batchid": "112sdtgs","payload": [[1, 2],[3, 4]]})
    assert response.status_code == 200
    assert response.json() == {"batchid": "112sdtgs","response": [3,7],"status": "complete","started_at": "2024-06-10T03:21:56.021246","completed_at": "2024-06-10T03:21:56.242891"
}

def test_addition_empty_list():
    response = client.post("/add", json={"batchid": "1shdhyfdt","payload": [[]]})
    assert response.status_code == 200
    assert response.json() == {"batchid": "1shdhyfdt","response": [0],"status": "complete","started_at": "2024-06-10T03:17:59.003062","completed_at": "2024-06-10T03:17:59.303987"
}



def test_addition_invalid_data():
    response = client.post("/add", json={"batchid": "invalid","payload": "invalid"})
    assert response.status_code == 422  # Unprocessable Entity
