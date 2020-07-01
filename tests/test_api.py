import pytest
from app import app

@pytest.fixture
def client():
  # Spin up test flask app
  app.config['TESTING'] = True
  return app.test_client()

def test_get_email(client):
  # SPARC Portal user info
  portal_user_id = 729
  portal_user_email = b'nih-data-portal@blackfynn.com'

  r = client.get(f"/get_email/{portal_user_id}")
  assert r.data == portal_user_email

  r = client.get(f"/get_email/{999999}")
  assert r.status_code == 404
