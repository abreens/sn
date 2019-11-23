import os
import pytest
from main import app, db
from models import User




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


# def test_index_wrong_password(client):
#    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
#                                "user-password": "wrongpassword"}, follow_redirects=True)
#    response = client.get('/login')
#    assert b'WRONG PASSWORD!' in response.data

def test_result_correct(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get the first (and only) user object from the database
    user = db.query(User).first()

    # set the secret number to 22, so that you can make a success "guess" in the test.
    user.secret_number = 22
    db.add(user)
    db.commit()

    response = client.post('/result', data={"guess": 22})  # enter the correct guess
    assert b'Het geheime nummer is inderdaad 22' in response.data


def test_result_te_klein(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get the first (and only) user object from the database
    user = db.query(User).first()

    # set the secret number to 22, so that you can make a success "guess" in the test.
    user.secret_number = 22
    db.add(user)
    db.commit()

    response = client.post('/result', data={"guess": 20})  # guess is too small
    assert b'try something bigger.' in response.data


def test_result_te_groot(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get the first (and only) user object from the database
    user = db.query(User).first()

    # set the secret number to 22, so that you can make a success "guess" in the test.
    user.secret_number = 22
    db.add(user)
    db.commit()

    response = client.post('/result', data={"guess": 24})  # guess is too big
    assert b'try something smaller.' in response.data


def test_result_out_of_bound_low(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get the first (and only) user object from the database
    user = db.query(User).first()

    # set the secret number to 22, so that you can make a success "guess" in the test.
    user.secret_number = 22
    db.add(user)
    db.commit()

    response = client.post('/result', data={"guess": 0})  # guess is out of bound
    assert b'Het getal moet tussen 1 en 30 liggen.' in response.data


def cleanup():
    # clean up/delete the DB (drop all tables in the database)
    db.drop_all()
