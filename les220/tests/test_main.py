import os
import pytest
from main import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    client = app.test_client()

    cleanup()  # clean up before every test

    db.create_all()

    yield client


def test_index_not_logged_in(client):
    response = client.get('/index')
    # This is the actual test
    assert b'Enter your name' in response.data


def test_index_logged_in(client):
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)
    response = client.get('/index')
    assert b'Uw gok?' in response.data


def cleanup():
    # clean up/delete the DB (drop all tables in the database)
    db.drop_all()