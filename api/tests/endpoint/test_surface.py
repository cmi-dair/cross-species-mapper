"""Endpoint tests for the surfaces router."""
from fastapi import status, testclient

from src import main

client = testclient.TestClient(main.app)


def test_get_hemispheres() -> None:
    """Test that the hemispheres are returned."""
    response = client.get(
        "/surfaces/hemispheres", params={"species": "human", "side": "left"}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json().keys() == {
        "iFaces",
        "jFaces",
        "kFaces",
        "name",
        "xCoordinate",
        "yCoordinate",
        "zCoordinate",
    }
