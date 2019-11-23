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


def test_home_page(client):
    response = client.get('/')
    assert b'/static/img/secretcode.jpg' in response.data


def test_index_not_logged_in(client):
    response = client.get('/index')
    # This is the actual test
    assert b'Enter your name' in response.data


def test_index_logged_in(client):
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)
    response = client.get('/index')
    assert b'Uw gok?' in response.data


def test_index_wrong_password(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # POST
    response = client.post('/login', data={"user-name": "TestUser",
                                           "user-email": "testuser@telenet.be",
                                           "user-password": "456"}, follow_redirects=True)
    assert b'WRONG PASSWORD!' in response.data


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


def test_result_out_of_bound_high(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get the first (and only) user object from the database
    user = db.query(User).first()

    # set the secret number to 22, so that you can make a success "guess" in the test.
    user.secret_number = 22
    db.add(user)
    db.commit()

    response = client.post('/result', data={"guess": 31})  # guess is out of bound
    assert b'Het getal moet tussen 1 en 30 liggen.' in response.data


def test_result_geen_getal(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get the first (and only) user object from the database
    user = db.query(User).first()

    # set the secret number to 22, so that you can make a success "guess" in the test.
    user.secret_number = 22
    db.add(user)
    db.commit()

    response = client.post('/result', data={"guess": "Axel"})  # guess is geen getal
    assert b'Dat was geen (geheel) getal.' in response.data


def test_myprofile(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)
    response = client.get('/profile')
    assert b'TestUser' in response.data


def test_profile_edit(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # GET
    response = client.get('/profile/edit')
    assert b'EDIT YOUR PROFILE' in response.data

    # POST
    response = client.post('/profile/edit', data={"profile-name": "TestUser2",
                                                  "profile-email": "testuser2@telenet.be",
                                                  "profile-password": "123"}, follow_redirects=True)
    assert b'TestUser2' in response.data
    assert b'testuser2@telenet.be' in response.data


def test_profile_delete(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)
    # GET
    response = client.get('/profile/delete')
    assert b'DELETE YOUR PROFILE' in response.data

    # POST
    response = client.post('/profile/delete', follow_redirects=True)
    assert b'/static/img/secretcode.jpg' in response.data  # redirected back to the index site


def test_all_users(client):
    response = client.get('/users')
    assert b'<H3>USERS</H3>' in response.data
    assert b'TestUser' not in response.data  # TestUser is not yet created

    # create a new user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    response = client.get('/users')
    assert b'<H3>USERS</H3>' in response.data
    assert b'TestUser' in response.data


def test_user_details(client):
    # create a new user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)

    # get user object from the database
    user = db.query(User).first()

    response = client.get('/user/{}'.format(user.id))
    assert b'testuser@telenet.be' in response.data
    assert b'TestUser' in response.data


def test_logout(client):
    # create a user
    client.post('/login', data={"user-name": "TestUser", "user-email": "testuser@telenet.be",
                                "user-password": "123"}, follow_redirects=True)
    # And then logout again
    response = client.get('/logout')
    assert b'/static/img/secretcode.jpg' in response.data


def cleanup():
    # clean up/delete the DB (drop all tables in the database)
    db.drop_all()
