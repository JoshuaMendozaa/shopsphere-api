from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    #test the /health endpoint
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "app_name" in data
    assert "app_version" in data

def test_docs_redirect(client: TestClient):
    #Test the /docs endpoint
    response = client.get("api/v1/docs")
    assert response.status_code == 200
    assert "Swagger UI" in response.text