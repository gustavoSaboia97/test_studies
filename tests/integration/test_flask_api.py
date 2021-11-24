import pytest
import requests


@pytest.mark.it("Person set data ok")
def test_get_health_info() -> None:
    response = requests.get('http://localhost:5000/health')

    assert response.ok
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
