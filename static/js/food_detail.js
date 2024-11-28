// Инициализация карты при загрузке страницы
var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Функция для отображения текущего местоположения
function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    map.setView([lat, lon], 13);

    L.marker([lat, lon]).addTo(map)
        .bindPopup('Your Location')
        .openPopup();

    // Логика для расчета стоимости доставки
    var deliveryCost = calculateDeliveryCost(lat, lon);
    var deliveryTime = calculateDeliveryTime(lat, lon);

    // Показать окно с выбором покупки
    if (confirm("Стоимость доставки: $" + deliveryCost + ". Хотите купить?")) {
        // Отправка запроса на сервер для обработки покупки
        fetch('/buy/' + foodId, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ delivery_cost: deliveryCost })
        })
        .then(response => response.json())
        .then(data => {
            alert("Товар куплен успешно! Время доставки: " + deliveryTime + " минут.");
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert("Покупка отменена.");
    }
}

// Функция для расчета стоимости доставки
function calculateDeliveryCost(lat, lon) {
    // Логика для расчета стоимости доставки
    // В реальном приложении здесь может быть более сложная логика
    var baseCost = 10; // Базовая стоимость доставки
    var distance = getDistanceFromLatLonInKm(lat, lon, 52.490203, 85.140387); // Пример координат ресторана
    var additionalCost = distance * 0.5; // Дополнительная стоимость за каждый километр
    return baseCost + additionalCost;
}

// Функция для расчета времени доставки
function calculateDeliveryTime(lat, lon) {
    // Логика для расчета времени доставки

    // В реальном приложении здесь может быть более сложная логика
    var distance = getDistanceFromLatLonInKm(lat, lon, 52.490203, 85.140387); // Пример координат ресторана
    var deliveryTime = distance * 2; // Пример: 2 минуты на километр
    return deliveryTime.toFixed(0); // Округление до целого числа
}

// Функция для расчета расстояния между двумя точками
function getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2) {
    var R = 6371; // Радиус Земли в километрах
    var dLat = deg2rad(lat2 - lat1);
    var dLon = deg2rad(lon2 - lon1);
    var a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var d = R * c; // Расстояние в километрах
    return d;
}

// Функция для преобразования градусов в радианы
function deg2rad(deg) {
    return deg * (Math.PI / 180);
}

// Обработчик нажатия на кнопку "Купить"
document.getElementById('buy-button').addEventListener('click', function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Этот браузер не поддерживает геолокацию.");
    }
});
