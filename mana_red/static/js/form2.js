
$(document).ready(function(){
    $('#submit').on('click',function(event){
         event.preventDefault();
         $.ajax({
            type: 'POST',
            url: "/waitlist/apply",
            headers: {
                "X-CSRFToken" : csrf,
                "Content-Type": "application/json"
            },
            data : JSON.stringify({ 
                email : $('#email').val(),
                howhear : $('#howhear').val(),
                }).replaceAll("',","',\n"),
            dataType : 'json',
            contentType : 'application/json',
            success: function (e) {
                alert('Thanks for joining our waitlist, '+$('#email').val()+'!');
                $('input').each(function(){$(this).val('');})
            },
            error: function (e) {
                alert('no');
            },
        });
    });
});
