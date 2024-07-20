$(document).ready(function(){
    // add to cart
    $('.add_to_cart').on('click', function(e){
        e.preventDefault();
        
        let food_id = $(this).attr('data-id');
        let url = $(this).attr('data-url');
       
        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                console.log(response);
                if(response.status == 'login_required'){
                    swal(response.message, '', 'info').then(function(){
                        window.location = '/login';
                    });
                }else if(response.status == 'Failed'){
                    swal(response.message, '', 'error');
                }else{
                    $('#cart_counter').html(response.cart_counter['cart_count']);
                    $('#qty-' + food_id).html(response.qty);

                    applycartamt(
                        response.cart_amount['subtotal'],
                        response.cart_amount['tax_dict'],
                        response.cart_amount['grand_total']
                    );
                } 
            },
        });
    });

    // place the cart item quantity on load
    $('.item_qty').each(function(){
        var the_id = $(this).attr('id');
        var qty = $(this).attr('data-qty');
        $('#' + the_id).html(qty);
    });

    // decrease cart
    $('.decrease_cart').on('click', function(e){
        e.preventDefault();
        
        let food_id = $(this).attr('data-id');
        let url = $(this).attr('data-url');
        let cart_id = $(this).attr('id'); 
        
        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                console.log(response);
                if(response.status == 'login_required'){
                    swal(response.message, '', 'info').then(function(){
                        window.location = '/login';
                    });
                }else if(response.status == 'Failed'){
                    swal(response.message, '', 'error');
                }else{
                    $('#cart_counter').html(response.cart_counter['cart_count']);
                    $('#qty-' + food_id).html(response.qty);

                    applycartamt(
                        response.cart_amount['subtotal'],
                        response.cart_amount['tax_dict'],
                        response.cart_amount['grand_total']
                    );

                    if(window.location.pathname == '/cart/'){
                        removecartitem(response.qty, cart_id);
                        checkemptycart();
                    }
                }
            },
        });
    });

    // delete cart
    $('.delete_cart').on('click', function(e){
        e.preventDefault();
        
        let cart_id = $(this).attr('data-id');
        let url = $(this).attr('data-url');
        
        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                console.log(response);
                if(response.status == 'Failed'){
                    swal(response.message, '', 'error');
                }else{
                    $('#cart_counter').html(response.cart_counter['cart_count']);
                    swal(response.status, response.message, "success");

                    applycartamt(
                        response.cart_amount['subtotal'],
                        response.cart_amount['tax_dict'],
                        response.cart_amount['grand_total']
                    );
                    removecartitem(0, cart_id);
                    checkemptycart();
                }
            },
        });
    });

    function removecartitem(cartitemqty, cart_id){
        if(window.location.pathname == '/cart/'){
            if(cartitemqty <= 0){
                document.getElementById("cart-item-" + cart_id).remove();
            }
        }
    }

    function checkemptycart(){
        var cart_counter = document.getElementById('cart_counter').innerHTML;
        if(cart_counter == 0){
            document.getElementById('empty-cart').style.display = "block";
        }
    }

    function applycartamt(subtotal, tax_dict, grand_total){
        if(window.location.pathname == '/cart/'){
            $('#subtotal').html(subtotal);
            $('#total').html(grand_total);


            for(key1 in tax_dict){
                for(key2 in tax_dict[key1]){
                    $('#tax-'+key1).html(tax_dict[key1][key2])
                }
            }
        }
    }

   
});
