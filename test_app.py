from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert b"Welcome to our website!" in response.data

def test_about(client):
    response = client.get('/about')
    assert b"About Us" in response.data

def test_contact(client):
    response = client.get('/contact')
    assert b"Contact Us" in response.data

def test_contact_form_submission(client):
    response = client.post('/contact', data=dict(
        name='John Doe',
        email='john@example.com',
        message='Hello, this is a test message.'
    ), follow_redirects=True)
    assert b"Thank you for contacting us, John Doe!" in response.data
