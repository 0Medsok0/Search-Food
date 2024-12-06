// document.addEventListener('DOMContentLoaded', function() {
//     const buttons = document.querySelectorAll('.button');
//     const products = document.querySelectorAll('.product');

//     buttons.forEach(button => {
//         button.addEventListener('click', function() {
//             const category = button.getAttribute('data-category');
//             products.forEach(product => {
//                 if (category === 'all' || product.getAttribute('data-category') === category) {
//                     product.style.display = 'block';
//                 } else {
//                     product.style.display = 'none';
//                 }
//             });
//         });
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.button');
    const products = document.querySelectorAll('.product');
    let visibleProducts = 4;

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const category = button.getAttribute('data-category');
            products.forEach(product => {
                if (category === 'all' || product.getAttribute('data-category') === category) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            });
        });
    });

    // Показать первые 4 продуктов
    products.forEach((product, index) => {
        if (index < visibleProducts) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });

    // Кнопка "Показать еще"
    const showMoreButton = document.createElement('button');
    showMoreButton.className = 'show-more';
    showMoreButton.textContent = 'Показать еще';
    document.querySelector('.sh-fd').appendChild(showMoreButton);

    showMoreButton.addEventListener('click', function() {
        visibleProducts += 4;
        products.forEach((product, index) => {
            if (index < visibleProducts) {
                product.style.display = 'block';
            }
        });
        if (visibleProducts >= products.length) {
            showMoreButton.style.display = 'none';
        }
    });
});
