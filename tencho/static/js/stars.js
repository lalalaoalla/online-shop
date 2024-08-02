let star = document.querySelectorAll('.star')// ищем все элементы star(классы то что), возвращают нам их списком

star.forEach((elem) => {// для каждого элемента в массиве star
    elem.addEventListener("click", () => {// дя каждого elem click будет началом действия, так скажем
        elem.classList.toggle("clicked")// Этот метод добавляет класс "clicked" к элементу, если он еще не был добавлен, и удаляет его, если он уже был добавлен.
        // Другими словами, он "переключает" наличие класса "clicked" на элементе.
    })
})


// ИСПОЛЬЗУЕТСЯ В product.html
