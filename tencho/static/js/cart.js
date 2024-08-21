$(document).ready(function(){//после загрузки полной
    var form = $('#form_buying_product');// с этой формой работаем
    console.log(form);//логи формы добавляем
    form.on('submit', function(e){//что будет после нажатия кнопки с отправлением
        e.preventDefault();//чтобы без перезагрузки
        //console.log('123');
        var nmb = $('#number').val();// значение нашего количества
        var size = $('#size').val();
        console.log(nmb);// если что его логи
        console.log(size);
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");//название
        var name = submit_btn.data("name");//имя
        var cost = submit_btn.data("cost");
        var category = submit_btn.data("category");
        console.log(product_id );
        console.log(name);
        console.log(cost);
        console.log(category);
    })

});

// let productammount = document.querySelector(".counter-value")//видмо количество товаров
// let buy = document.querySelector(".order-block a")//наверное это блок "Купить"
// let productsize = document.querySelectorAll(".product-sizes div")//элемент позволяющий выбрать размер


// function addtocart(e) {//вызывается при кликанье на кнопочку купить
//     //как бы ну мы все заносим в корзину(берем из нашего лок хранилища)
//     let obj = new Object()
//     let mas = []
//     obj.img = localStorage.getItem("img")
//     obj.name = localStorage.getItem("name")
//     obj.price = localStorage.getItem("price")
//     obj.category = localStorage.getItem("category")
//     obj.ammount = Number(productammount.textContent)//выбранное количество
//     obj.size = e.getAttribute("data-size")//выбранный размер

//     let isExist = localStorage.getItem("cart-items")//проверка есть ли у нас в корзине что-то

//     if(isExist) {//если есть, то мы добавляем наш товар к тому что есть
//         let existedmas = JSON.parse(localStorage.getItem("cart-items"))
//         existedmas.push(obj)//если есть, то 
//         localStorage.setItem("cart-items", JSON.stringify(existedmas))
//     }else if(!isExist) {//если нет то мы добавляем наш товар
//         mas.push(obj)
//         localStorage.setItem("cart-items", JSON.stringify(mas))
//     }
// }

// // productsize.forEach((elem) => {//короче тут кликаем по размеру
// //     elem.addEventListener("click", () => {
// //         if (elem.classList.contains("clicked")) {//если мы кликнули
// //             buy.setAttribute("data-size", elem.textContent)//то добавляем атрибуту data-size наш размер
// //             buy.classList.add("enabled")//делаем кнопку купить активной
// //             document.querySelector(".product-price").nextElementSibling.classList.remove("SizeError")//удаляем ошибку(ну то что размер не отмечен)
// //         }else if(!elem.classList.contains("clicked")) {//ну ту если размер не выбран, то мы не можем нажать купить
// //             document.querySelector(".product-price").nextElementSibling.classList.add("SizeError")
// //             buy.classList.remove("enabled")
// //         }
// //     })
// // })

// //ИСПОЛЬЗУЕТСЯ В product.html
