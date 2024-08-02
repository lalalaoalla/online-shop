function reloadfilter(e) {//e- когда мы тыкаем на кнопочку категории товара
  $.getJSON('/jsons/products.json', function (data) {
    let out = ''
    $('.catalogue-items-list').innerHTML = ''
    for (let key in data) {
      if (data[key].category == e.getAttribute("data-category")) {//проверяем, совпадает ли категория нашего товара с категорией на которую мы тыкнули
        out += '<div class="item">'
        out += '<div class="item-content">'
        out += '<span class="detailed" onclick="modalWindow(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Подробнее</span>'
        out += '<img src="' + data[key].image + '" alt="' + data[key].name + '">'
        out += '<div class="underline"></div>'
        out += '<p class="item-title">' + data[key].name + '</p>'
        out += '<p class="price">Цена: ' + data[key].cost + '₽</p>'
        out += '<a href="product.html" onclick="buy(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Купить</a>'
        out += '</div>'
        out += '</div>'
      }
    }
    $('.catalogue-items-list').html(out)// типа обновляем потом
  })
}

document.querySelector(".clear").addEventListener("click", () => {// для кнопки очистить

  categories.forEach((elem) => {// типа проходим по всем категориям
    elem.classList.remove("clicked")//и удаляем тыкания на них?
  })

  $.getJSON('/jsons/products.json', function (data) {
    let out = ''
    $('.catalogue-items-list').innerHTML = ''
    for (let key in data) {
      out += '<div class="item">'
      out += '<div class="item-content">'
      out += '<span class="detailed" onclick="modalWindow(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Подробнее</span>'
      out += '<img src="' + data[key].image + '" alt="' + data[key].name + '">'
      out += '<div class="underline"></div>'
      out += '<p class="item-title">' + data[key].name + '</p>'
      out += '<p class="price">Цена: ' + data[key].cost + '₽</p>'
      out += '<a href="product.html" onclick="buy(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Купить</a>'
      out += '</div>'
      out += '</div>'
    }
    $('.catalogue-items-list').html(out)
  })
})

let categories = document.querySelectorAll(".categories")//считываем все категории
let catIsClicked = false//отслеживаем, выбрана ли сейчас какая-то категория

categories.forEach((elem) => {
  elem.addEventListener("click", () => {//опять все смотрим по клику
    for(let item of categories) {//сбрасываем выбор всех ранее выбранных категорий
      item.classList.remove("clicked")
    }

    if(!catIsClicked) {// короче если сейчас не выбрана ни одна категория то тыкаем ок появляет
      elem.classList.toggle("clicked")
      catIsClicked = true
    }else if (catIsClicked) {// иначе 
      elem.classList.toggle("clicked")
      catIsClicked = false
    }
  })
})

//ИСПОЛЬЗУЕТСЯ В catalogue.html