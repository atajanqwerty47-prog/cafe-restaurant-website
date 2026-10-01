# Cafe Royal - Premium Restaurant Website

Современный, красивый и функциональный сайт для премиального кафе/ресторана.

## Особенности

✨ **Дизайн**
- Премиальный, современный дизайн
- Полностью адаптивный (мобильный, планшет, десктоп)
- Быстрая загрузка
- SEO оптимизирован

🍽️ **Функции**
- Меню с описанием блюд и ценами
- Фотогалерея
- Информация о кафе
- Отзывы гостей
- Контактная форма
- Мобильное меню
- Быстрые ссылки для звонка

📱 **Контакты**
- Телефон: +993 65 555 55
- Адрес: 11 микрорайон
- Часы: 09:00 - 23:00 ежедневно

## Установка

```bash
pip install -r requirements.txt
python app.py
```

Сайт будет доступен по адресу: `http://localhost:10000`

## Развертывание

### PythonAnywhere
1. Загрузить проект
2. Установить зависимости
3. Настроить Web app
4. Получить публичную ссылку

### Render.com
1. Подключить GitHub repo
2. Настроить build command: `pip install -r requirements.txt`
3. Start command: `python app.py`
4. Deploy

## Структура проекта

```
cafe-restaurant-website/
├── app.py                 # Flask приложение
├── requirements.txt        # Зависимости
├── templates/
│   └── index.html         # Главная страница
├── static/
│   ├── style.css          # Стили
│   └── script.js          # JavaScript
└── README.md
```

## Кастомизация

- Меню: редактируй `products` в `app.py`
- Отзывы: редактируй `posts` в `app.py`
- Цвета: измени CSS переменные в `static/style.css`
- Текст: редактируй `templates/index.html`

## Лицензия

© 2025 Cafe Royal. Все права защищены.
