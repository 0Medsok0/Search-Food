# pytest -v tests.py

import pytest
from flask import url_for
from index import app, db, Food, Store, Order

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'store' in response.data
    assert b'food' in response.data

def test_store_detail(client):
    with app.app_context():
        store = Store(name='Test Store', description='Test Description')
        db.session.add(store)
        db.session.commit()
        store_id = store.id

    response = client.get(f'/store/{store_id}')
    assert response.status_code == 200
    assert b'Test Store' in response.data

def test_food_detail(client):
    with app.app_context():
        store = Store(name='Вкусняшкин', description='Лучший магазин еды в городе')
        db.session.add(store)
        db.session.commit()
        store_id = store.id

        food = Food(name='Пицца', description='Томатный соус, моцарелла, пепперони', delivery_time='30 min', store_id=store_id, category='Test Category')
        db.session.add(food)
        db.session.commit()
        food_id = food.id

    response = client.get(f'/food/{food_id}')
    assert response.status_code == 200
    assert 'Пицца'.encode('utf-8') in response.data

def test_buy_food(client):
    with app.app_context():
        store = Store(name='Test Store', description='Test Description')
        db.session.add(store)
        db.session.commit()
        store_id = store.id

        food = Food(name='Test Food', description='Test Description', delivery_time='30 min', store_id=store_id, category='Test Category')
        db.session.add(food)
        db.session.commit()
        food_id = food.id

    response = client.post(f'/buy/{food_id}', json={'delivery_cost': 10.0})
    assert response.status_code == 200
    assert b'Food bought successfully' in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'about' in response.data

def test_vacancies(client):
    response = client.get('/vacancies')
    assert response.status_code == 200
    assert b'vacancies' in response.data

def test_apply(client):
    response = client.get('/apply')
    assert response.status_code == 200
    assert b'resume' in response.data

def test_resume_post(client):
    response = client.post('/resume', data={'name': 'Test Name', 'email': 'test@example.com', 'message': 'Test Message'})
    assert response.status_code == 302
    assert response.location.endswith(url_for('apply'))

def test_resume_get(client):
    response = client.get('/resume')
    assert response.status_code == 200
    assert b'resume' in response.data


