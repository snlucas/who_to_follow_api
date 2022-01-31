from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_user_by_stars():
    """
    Test if read all is working,
    even without any post.
    """
    technology = "FastAPI"
    response = client.get("/{technology}/stars")
    assert response.status_code == 200
    assert response.json() is not None