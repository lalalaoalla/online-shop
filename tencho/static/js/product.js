function buy(e) {//вроде как это должна быть функция, которая хранит информацию о товаре(когда вот мы кликали)
    localStorage.setItem("name",e.getAttribute("data-name"))//из e мы получаем поле data-name и сохраняем его в хранилище браузера под именем name
    localStorage.setItem("price",e.getAttribute("data-cost"))
    localStorage.setItem("img",e.getAttribute("data-img"))
    localStorage.setItem("about",e.getAttribute("data-desc"))
    localStorage.setItem("category",e.getAttribute("data-category"))
}


//ИСПОЛЬЗУЕТСЯ В catalogue.html index.html
