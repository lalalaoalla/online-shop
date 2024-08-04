$('document').ready(function(){// обе функции выполняются только после полной загрузки страницы

    loadpr()
    loadnew()

});

function loadpr() {
  $.ajax({
    url: 'api/v1/productlist_index/',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
        let out = ''
        for (let key in data){
          if (key < 12) {// выводит первые 12 товаров просто(по крайней мере в данный момент)
            out+='<div class="item">'
            out+='<div class="item-content">'
            out+='<span class="detailed" onclick="modalWindow(this)" data-name="'+data[key].name+'" data-cost="'+data[key].cost+'"  data-img="'+data[key].image+'" data-desc="'+data[key].description+'" data-category="'+data[key].category+'">Подробнее</span>'
            out+='<img src="'+data[key].image+'" alt="'+data[key].name+'">'
            out+='<div class="underline"></div>'
            out+='<p class="item-title">'+data[key].name+'</p>'
            out+='<p class="price">Цена: '+data[key].cost+'₽</p>'
            out+='<a href="product.html" onclick="buy(this)" data-name="'+data[key].name+'" data-cost="'+data[key].cost+'"  data-img="'+data[key].image+'" data-desc="'+data[key].description+'" data-category="'+data[key].category+'">Купить</a>'
            out+='</div>'
            out+='</div>'
          }
      }
    $('.items').html(out)
    }
  });
}

function loadnew() {
  $.ajax({
    url: 'api/v1/productlist_index_new/',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
        let out = ''
        for (let key in data){
            out+='<div class="slider-item">'
            out+='<div class="slider-item-content">'
            out+='<span class="detailed" onclick="modalWindow(this)" data-name="'+data[key].name+'" data-cost="'+data[key].cost+'"  data-img="'+data[key].image+'" data-desc="'+data[key].description+'" data-category="'+data[key].category+'">Подробнее</span>'
            out+='<img src="'+data[key].image+'" alt="'+data[key].name+'">'
            out+='<div class="slider-info">'
            out+='<h1 class="slider-item-title">'+data[key].name+'</h1>'
            out+='<p class="price">Цена: '+data[key].cost+'₽</p>'
            out+='<a class="slider-buy-btn" href="product.html" onclick="buy(this)" data-name="'+data[key].name+'" data-cost="'+data[key].cost+'"  data-img="'+data[key].image+'" data-desc="'+data[key].description+'" data-category="'+data[key].category+'">Купить</a>'
            out+='</div>'
            out+='</div>'
            out+='</div>'
      }
    $('.slider-track').html(out)
    }
  });
}

//атрибуты с onclick это вункции, которые вызываются при данном событии
// `data-name`,  `data-cost`,  `data-img`,  `data-desc`,  `data-category`  -  это  атрибуты  данных,  которые  хранят  информацию  о  товаре.  
//Эти  данные  могут  использоваться  в  функциях  `modalWindow()`  и  `buy()`  для  обработки  событий.



//ПРИМЕНЯЕТСЯ В index.html