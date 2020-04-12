
//get email when button is clicked
$("#emailSubmit").click(function(){
  console.log($("#emailIn").val())
  testAjax()
});

//ajax to view to submit email to server
function testAjax() {
    $.ajax({
      url: "email",
      success: function(data) {
         console.log('You did it');
      }
   });
}
