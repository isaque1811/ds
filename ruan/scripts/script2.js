function animateProduct(product) {
    product.classList.add('animate');
    
    setTimeout(() => {
        product.classList.remove('animate');
    }, 500); // Duração da animação
}
let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');

function showSlide(index) {
    items.forEach((item, i) => {
        item.classList.remove('active');
        if (i === index) {
            item.classList.add('active');
        }
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % items.length;
    showSlide(currentIndex);
}

setInterval(nextSlide, 3000); // Muda o slide a cada 3 segundos
showSlide(currentIndex);
