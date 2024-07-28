$('document').ready(function(){// опять же гарантируем, что эта функция будет выполняться только после полной загрузки html страницы
    loadall()// обозначение нашей функции, она подгружает все и вообще о ней дальше
})


function loadall() {
    $.getJSON('/jsons/products.json', function (data) {//сначала - функция из jQuery, подгружаем наши данные, data - содержит наши полученные данные
          let out = ''//будет использоваться для сохранения HTML кода товаров(пока не особо догоняю)
          for (let key in data){//собственно, просто переборка каждого элемента в наших данных
            //строки далее включают html код, то есть каждый товар генерируется вот так красиво
            //такс это надо будет еще глянуть, конечно, как потом поменять вот это вот немного, хотя в целом понятно, главное считать по-другому
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
      $('.catalogue-items-list').html(out)//первая часть ищет данный код на странице(типа если его нашли, значит нужно вставлять вот это), вторая запускает out
    })
}
//атрибуты с onclick это вункции, которые вызываются при данном событии
// `data-name`,  `data-cost`,  `data-img`,  `data-desc`,  `data-category`  -  это  атрибуты  данных,  которые  хранят  информацию  о  товаре.  
//Эти  данные  могут  использоваться  в  функциях  `modalWindow()`  и  `buy()`  для  обработки  событий.



//ПРИМЕНЯЕТСЯ В catalogue.html