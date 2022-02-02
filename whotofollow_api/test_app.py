from chalice.test import Client
from app import app

client = Client(app)


def test_get_user_by_stars():
    """
    Test if read all is working,
    even without any post.
    """
    with client:
        technology = "FastAPI"
        response = client.http.get("/{technology}/stars")
        assert response.status_code == 200
        assert response.json_body is not None
