$(document).ready(function(){

  $('#total').val("$0.00");

  $('#shirt').on("blur", function(){

    shirt_quantity = $('#shirt').val()
    var total = 1;
    total = 3.99 * shirt_quantity;
    $('#total').val(total);
  })


});

function done(){

  swal({
  icon: "success",
  text: "Order Successfully Submitted",
});
}
