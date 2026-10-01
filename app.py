from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Bistro Burger", "price": "32000", "category": "Бургеры", "desc": "Говядина, сыр, лук, томат, соус"},
    {"id": 2, "name": "Cappuccino", "price": "15000", "category": "Кофе", "desc": "Ароматный кофе с воздушной пенкой"},
    {"id": 3, "name": "Pasta Carbonara", "price": "39000", "category": "Основные блюда", "desc": "Спагетти, сливочный соус, пармезан"},
    {"id": 4, "name": "Cheesecake", "price": "18000", "category": "Десерты", "desc": "Нежный сливочный десерт с ягодами"},
    {"id": 5, "name": "Latte", "price": "17000", "category": "Кофе", "desc": "Плотный вкус с мягкой текстурой"},
    {"id": 6, "name": "Caesar Salad", "price": "30000", "category": "Салаты", "desc": "Курица, листья салата, сыр, гренки"},
    {"id": 7, "name": "Seafood Pasta", "price": "42000", "category": "Основные блюда", "desc": "Морепродукты в нежном соусе"},
    {"id": 8, "name": "Affogato", "price": "16000", "category": "Десерты", "desc": "Эспрессо с ванильным мороженым"}
]

posts = [
    {"id": 1, "title": "Наша кухня — это эмоции", "text": "Каждая тарелка готовится с любовью и вниманием к деталям, чтобы вы почувствовали вкус настоящего уюта.", "author": "Шеф-повар"},
    {"id": 2, "title": "Топ-5 напитков сезона", "text": "Летние и осенние рецепты кофе, смузи и авторских миксов, которые обязательно стоит попробовать.", "author": "Бармен"},
    {"id": 3, "title": "Как мы создаем атмосферу", "text": "Теплый свет, музыка, натуральные материалы и уютные зоны помогают каждому гостю расслабиться и забыть о суете.", "author": "Менеджер"}
]

@app.route('/')
def index():
    return render_template('index.html', products=products, posts=posts)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
