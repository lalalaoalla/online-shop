window.onload = () => {//вызываем после загрузки страницы
  document.querySelector(".product-img").src = localStorage.getItem("img")//получчаем url нашей картинки
  document.querySelector(".product-title").innerHTML = localStorage.getItem("name")
  document.querySelector(".product-price").innerHTML = "Цена: " + localStorage.getItem("price") + "₽"
  document.querySelector(".product-item-about").innerHTML = localStorage.getItem("about")
  loadsame()
}

function loadsame() {
  $.getJSON('/jsons/products.json', function (data) {
    let out = ''//сюда собирается html код
    let counter = 1
    for (let key in data) {
      if (data[key].category == localStorage.getItem("category") && counter < 4) {// проверяем совпадает ли 
        //категория нашего товара с товаром из данных и выводим первые 3
        out += '<div class="item">'
        out += '<div class="item-content">'
        out += '<span class="detailed" onclick="modalWindow(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Подробнее</span>'
        out += '<img src="' + data[key].image + '" alt="' + data[key].name + '">'
        out += '<div class="underline"></div>'
        out += '<p class="item-title">' + data[key].name + '</p>'
        out += '</div>'
        out += '</div>'
        counter++
      }
    }
    $('.new-items').html(out)
  })
}

//разобраться кто же у нас localStorage
//ИСПОЛЬЗУЕТСЯ В product.html