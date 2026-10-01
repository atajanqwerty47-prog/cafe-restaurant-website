document.querySelector('.contact-form')?.addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Спасибо! Ваша заявка принята. Мы свяжемся с вами в ближайшее время.');
    this.reset();
});

document.querySelector('.nav-btn')?.addEventListener('click', function () {
    alert('Бронирование столика: +998 (71) 123-45-67');
});

document.querySelectorAll('.menu-item button').forEach(function (button) {
    button.addEventListener('click', function () {
        alert('Спасибо! Заказ добавлен в корзину.');
    });
});
