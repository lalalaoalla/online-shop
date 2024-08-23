$(document).ready(function(){

    function basket_delete(basket_id){
        var data = {};
        data.basket_id = basket_id;

        var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    var data_del = {
      basket_id: basket_id,
      csrfmiddlewaretoken: csrf_token,
    };

    $.ajax({
      url: '/orders/basket/delete/', // Correct URL to your view
      type: 'POST',
      data: data_del,
      cache: false,
      success: function(data) {
        // Handle success (e.g., update the table or display a message)
        console.log("Basket item deleted successfully");
        // Reload the current basket view after deletion
        location.reload();
      },
      error: function() {
        console.log("Error deleting basket item");
      },
    });
  };
    
   var form = $('#form_delete_product');// с этой формой работаем
     console.log(form);//логи формы добавляем
     form.on('submit', function(e){//что будет после нажатия кнопки с отправлением
         e.preventDefault();//чтобы без перезагрузки

         var submit_btn = $('#submit_btn');// при нажатии на кнопку удалить
         var basket_id =  submit_btn.data("basket_id");// передаем id того, что нужно удалить

//         console.log(basket_id );

        basket_delete(basket_id);
    })
});
// используется в cart.html