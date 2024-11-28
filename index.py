from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'
db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    delivery_time = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(200), nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200), nullable=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_cost = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    stores = Store.query.all()
    return render_template('home.html', stores=stores)

@app.route('/store/<int:store_id>')
def store_detail(store_id):
    store = Store.query.get_or_404(store_id)
    foods = Food.query.filter_by(store_id=store_id).all()
    return render_template('store_detail.html', store=store, foods=foods)

@app.route('/food/<int:food_id>')
def food_detail(food_id):
    food = Food.query.get_or_404(food_id)
    return render_template('food_detail.html', food=food)

@app.route('/buy/<int:food_id>', methods=['POST'])
def buy_food(food_id):
    food = Food.query.get_or_404(food_id)
    delivery_cost = request.json.get('delivery_cost')

    if delivery_cost is None:
        return jsonify({'error': 'Delivery cost is required'}), 400

    new_order = Order(food_id=food.id, delivery_cost=delivery_cost)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Food bought successfully', 'food': food.name, 'delivery_cost': delivery_cost})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/vacancies')
def vacancies():
    return render_template('vacancies.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
