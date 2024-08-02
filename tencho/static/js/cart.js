let productammount = document.querySelector(".counter-value")//видмо количество товаров
let buy = document.querySelector(".order-block a")//наверное это блок "Купить"
let productsize = document.querySelectorAll(".product-sizes div")//элемент позволяющий выбрать размер

function addtocart(e) {//вызывается при кликанье на кнопочку купить
    //как бы ну мы все заносим в корзину(берем из нашего лок хранилища)
    let obj = new Object()
    let mas = []
    obj.img = localStorage.getItem("img")
    obj.name = localStorage.getItem("name")
    obj.price = localStorage.getItem("price")
    obj.category = localStorage.getItem("category")
    obj.ammount = Number(productammount.textContent)//выбранное количество
    obj.size = e.getAttribute("data-size")//выбранный размер

    let isExist = localStorage.getItem("cart-items")//проверка есть ли у нас в корзине что-то

    if(isExist) {//если есть, то мы добавляем наш товар к тому что есть
        let existedmas = JSON.parse(localStorage.getItem("cart-items"))
        existedmas.push(obj)//если есть, то 
        localStorage.setItem("cart-items", JSON.stringify(existedmas))
    }else if(!isExist) {//если нет то мы добавляем наш товар
        mas.push(obj)
        localStorage.setItem("cart-items", JSON.stringify(mas))
    }
}

productsize.forEach((elem) => {//короче тут кликаем по размеру
    elem.addEventListener("click", () => {
        if (elem.classList.contains("clicked")) {//если мы кликнули
            buy.setAttribute("data-size", elem.textContent)//то добавляем атрибуту data-size наш размер
            buy.classList.add("enabled")//делаем кнопку купить активной
            document.querySelector(".product-price").nextElementSibling.classList.remove("SizeError")//удаляем ошибку(ну то что размер не отмечен)
        }else if(!elem.classList.contains("clicked")) {//ну ту если размер не выбран, то мы не можем нажать купить
            document.querySelector(".product-price").nextElementSibling.classList.add("SizeError")
            buy.classList.remove("enabled")
        }
    })
})

//ИСПОЛЬЗУЕТСЯ В product.html
