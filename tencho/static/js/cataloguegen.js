$('document').ready(function(){// опять же гарантируем, что эта функция будет выполняться только после полной загрузки html страницы
    loadall()// обозначение нашей функции, она подгружает все и вообще о ней дальше
})


function loadall() {
  $.ajax({
      url: 'api/v1/productlist_in_catalogue/',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
          let out = '';
          for (let key in data) {
              out += '<div class="item">';
              out += '<div class="item-content">';
              out += '<span class="detailed" onclick="modalWindow(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Подробнее</span>';
              out += '<img src="' + data[key].image + '" alt="' + data[key].name + '">'; // Используем data[key].image
              out += '<div class="underline"></div>';
              out += '<p class="item-title">' + data[key].name + '</p>';
              out += '<p class="price">Цена: ' + data[key].cost + '₽</p>';
              out += '<a href="/product_detail/'+data[key].id+'" onclick="buy(this)" data-name="' + data[key].name + '" data-cost="' + data[key].cost + '"  data-img="' + data[key].image + '" data-desc="' + data[key].description + '" data-category="' + data[key].category + '">Купить</a>';
              out += '</div>';
              out += '</div>';
          }
          $('.catalogue-items-list').html(out);
      }
  });
}
//атрибуты с onclick это вункции, которые вызываются при данном событии
// `data-name`,  `data-cost`,  `data-img`,  `data-desc`,  `data-category`  -  это  атрибуты  данных,  которые  хранят  информацию  о  товаре.  
//Эти  данные  могут  использоваться  в  функциях  `modalWindow()`  и  `buy()`  для  обработки  событий.



//ПРИМЕНЯЕТСЯ В catalogue.html