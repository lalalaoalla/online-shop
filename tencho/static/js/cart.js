var fillForm;

$(document).ready(function(){//после загрузки полной
    

    function basketUpdating(product_id, quantity,size, cost,is_delete){
        var data = {};//какие-то наши передаваемые данные
            data.product_id = product_id;// ну добавили то, что у нас есть
            data.quantity = quantity;
            data.size = size;
            data.cost = parseInt(cost);
            
            // csrf наше
            if (is_delete=false){
                var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
             data["csrfmiddlewaretoken"] = csrf_token;
            }
             

             if (is_delete=true){
                var csrf_token = $('#form_delete_product [name="csrfmiddlewaretoken"]').val();
                data["csrfmiddlewaretoken"] = csrf_token;
                data["is_delete"] = true;
            }

            //url откуда считываем
             var url = form.attr("action");
    
            console.log(data)
             $.ajax({
                 url: url,
                 type: 'POST',
                 data: data,
                 cache: false,
                 success: function (data) {
                     console.log("OK");
                     window.location.href = 'http://127.0.0.1:8001/orders/';
    
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

        basketUpdating(product_id, quantity, size, cost, is_delete=false)

        
    })
    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id")
        quantity = 0;
        size = 0;
        cost=0;

        basketUpdating(product_id, quantity, size, cost, is_delete=true)
    })
});

fillForm = function (button) {
    document.getElementById('size').value = button.value;
}


// //ИСПОЛЬЗУЕТСЯ В product.html
