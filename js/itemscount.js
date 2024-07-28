let plus = document.querySelectorAll(".plus")// выбираем все элементы +
let minus = document.querySelectorAll(".minus")//все элементы -

minus.forEach((elem) => {//проходим по всем элементам
    elem.addEventListener("click", () => {//обработчик для каждого элемента это клик
        //типа если следующий элемент > 1
        if (elem.nextElementSibling.textContent > 1) {// наше число в поле должно быть не менее одного
            elem.nextElementSibling.innerHTML = Number(elem.nextElementSibling.textContent) - 1//уменьшаем значение элемента
        }
    })
})

//то же самое, правда зачем условие < 9, наверное нельзя тип оптом заказать
plus.forEach((elem) => {
    elem.addEventListener("click", () => {
        if (elem.previousElementSibling.textContent < 9) {
            elem.previousElementSibling.innerHTML = Number(elem.previousElementSibling.textContent) + 1
        }
    })
})

//ИСПОЛЬЗУЕТСЯ В cart.html, product.html
