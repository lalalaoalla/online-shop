window.onload = () => {//вызываем после загрузки страницы
  document.querySelector(".product-img").src = localStorage.getItem("img")//получчаем url нашей картинки
  document.querySelector(".product-title").innerHTML = localStorage.getItem("name")
  document.querySelector(".product-price").innerHTML = "Цена: " + localStorage.getItem("price") + "₽"
  document.querySelector(".product-item-about").innerHTML = localStorage.getItem("about")
  loadsame()
}

function loadsame() {
  $.ajax({
    url:'api/v1/productlist_in_one_category/',
    type: 'GET', 
    dataType: 'json', 
    success: function (data) {
    let out = ''//сюда собирается html код
    let counter = 1
    for (let key in data) {
      if (data[key].category == localStorage.getItem("category") && counter < 4 && data[key].name != localStorage.getItem("name")) {// проверяем совпадает ли 
        //категория нашего товара с товаром из данных и выводим первые 3
        out += '<div class="item">'
        out += '<div class="item-content">'
        out += '<span class="detailed" onclick="modalWindow(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Подробнее</span>'
        out += '<img src="' + data[key].image + '" alt="' + data[key].name + '">'
        out += '<div class="underline"></div>'
        out += '<p class="item-title">' + data[key].name + '</p>'
        out+='<a href="/product_detail/'+data[key].id+'" onclick="buy(this)" data-name="'+data[key].name+'" data-cost="'+data[key].cost+'"  data-img="'+data[key].image+'" data-desc="'+data[key].description+'" data-category="'+data[key].category+'">Купить</a>'
        out += '</div>'
        out += '</div>'
        counter++
      }
    }
    $('.new-items').html(out)
  }
  });
}

//разобраться кто же у нас localStorage
//ИСПОЛЬЗУЕТСЯ В product.html