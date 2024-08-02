let btn = document.querySelectorAll(".detailed")
let modal = document.querySelector(".zoom-modal")
let close = document.querySelector(".close")
let sizes = document.querySelectorAll(".sizes div")
let backbtn = document.querySelector('.back-btn')
//конкретно переменные выше берутся не в самом коде html, он находится в коде js тоже через out добавлялось
//например catalogue.js createcards.js 
let isClicked = false//отслеживание нажимали на кнопку уже или нет


function modalWindow(e) {
    showModal()//функция, определенная ниже
    // в общем опять записываем данные того, на что мы тыкнули в локальную штуку браузера
    //то что у нас под data-name будет стоять name
    localStorage.setItem("name",e.getAttribute("data-name"))
    localStorage.setItem("price",e.getAttribute("data-cost"))
    localStorage.setItem("img",e.getAttribute("data-img"))
    localStorage.setItem("about",e.getAttribute("data-desc"))
    localStorage.setItem("category",e.getAttribute("data-category"))
    //обозначаем короче что мы ставим когда нажимаем на подробнее вот атрибуты того, куда тыкнули

    document.querySelector(".modal-image").src = localStorage.getItem("img")
    document.querySelector(".modal-title").innerHTML = localStorage.getItem("name")
    document.querySelector(".modal-price").innerHTML = "Цена: " + localStorage.getItem("price") + "₽"
    document.querySelector(".modal-item-about").innerHTML = localStorage.getItem("about")
    // видимо то, что передается когда мы нажимаем после просмотра подробнее кнопочку купить
    document.querySelector(".modal-buy").setAttribute("data-img",localStorage.getItem("img"))
    document.querySelector(".modal-buy").setAttribute("data-name",localStorage.getItem("name"))
    document.querySelector(".modal-buy").setAttribute("data-cost",localStorage.getItem("price"))
    document.querySelector(".modal-buy").setAttribute("data-desc",localStorage.getItem("about"))
    document.querySelector(".modal-buy").setAttribute("data-category",localStorage.getItem("category"))

    document.querySelector(".modal-content").classList.add("showing")//вероятнее всего отвечает за анимацию появления окна контента
    //Устанавливает таймер на 5 секунд. 
    //По истечении этого времени удаляет класс "showing" из элемента с классом "modal-content", возможно, для анимации закрытия модального окна.
    setTimeout(() => {
        document.querySelector(".modal-content").classList.remove("showing")
    }, 5000)
}
close.addEventListener("click", () => {//типа это кнопочка, для появления анимации закрытия
    document.querySelector(".modal-content").classList.add("closing")
    setTimeout(() => {
        hideModal()
        document.querySelector(".modal-content").classList.remove("closing")
    }, 500)
})

sizes.forEach((elem) => {// это используется для тыкания на размеры и их выделения
    elem.addEventListener("click", () => {
        for (let item of sizes) {
            item.classList.remove("clicked")
        }

        if (!isClicked) {
            elem.classList.add("clicked")
            isClicked = true
        } else if (isClicked) {
            elem.classList.remove("clicked")
            isClicked = false
        }
    })
})


function showModal() {//отвечает за отображение модального окна
    modal.classList.toggle("open-modal")
    body.classList.toggle("open-modal")
    backbtn.style.display = "none"
}

function hideModal() {// отвечает за закрытие окна
    modal.classList.toggle("open-modal")
    body.classList.toggle("open-modal")
    backbtn.style.display = ""
}

//ИСПОЛЬЗУЕТСЯ В catalogue.html index.html product.html