from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Хот-дог", "price": "25000", "category": "Бургеры"},
    {"id": 2, "name": "Капучино", "price": "15000", "category": "Кофе"},
    {"id": 3, "name": "Паста Карбонара", "price": "35000", "category": "Основные блюда"},
    {"id": 4, "name": "Чизкейк", "price": "18000", "category": "Десерты"},
    {"id": 5, "name": "Латте", "price": "17000", "category": "Кофе"},
    {"id": 6, "name": "Салат Цезарь", "price": "30000", "category": "Салаты"},
]

posts = [
    {"id": 1, "title": "Путешествие по вкусам", "text": "Наша кухня сочетает свежие продукты и уютную атмосферу.", "author": "Admin"},
    {"id": 2, "title": "JavaScript советы", "text": "10 полезных трюков JS для красивых интерфейсов.", "author": "Admin"},
    {"id": 3, "title": "CSS макеты", "text": "Грид и Flexbox практика для современных страниц.", "author": "Admin"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products, posts=posts)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
