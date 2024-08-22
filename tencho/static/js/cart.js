var fillForm;

$(document).ready(function(){//после загрузки полной
    

    function basketUpdating(product_id, quantity, size, cost){
        var data = {};//какие-то наши передаваемые данные
            data.product_id = product_id;// ну добавили то, что у нас есть
            data.quantity = quantity;
            data.size = size;
            data.cost = parseInt(cost);
            // csrf наше
             var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
             data["csrfmiddlewaretoken"] = csrf_token;
            //url откуда считываем
             var url = form.attr("action");
    
            console.log(data)
             $.ajax({
                 url: url,
                 type: 'POST',
                 data: data,
                 cache: true,
                 success: function (data) {
                     console.log("OK");
                    
    
                 },
                 error: function(){
                     console.log("error")
                 }
             })
            }
            
            
    var form = $('#form_buying_product');// с этой формой работаем
    console.log(form);//логи формы добавляем
    form.on('submit', function(e){//что будет после нажатия кнопки с отправлением
        e.preventDefault();//чтобы без перезагрузки
        //console.log('123');
        var quantity = $('#number').val();// значение нашего количества
        var size = $('#size').val();
        console.log(quantity);// если что его логи
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

        basketUpdating(product_id, quantity, size, cost)

        
    })
});

fillForm = function (button) {
    document.getElementById('size').value = button.value;
}


// //ИСПОЛЬЗУЕТСЯ В product.html
