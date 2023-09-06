
$(document).ready(function(){
    $('#submit').on('click',function(){
        console.log('ha');
        $.ajax({
            type: 'POST',
            url: "/internship/apply",
            headers: {
                "X-CSRFToken" : csrf,
                "Content-Type": "application/json"
            },
            data : JSON.stringify({}), // { data1 : $('#1').val()},
            dataType : 'json',
            contentType : 'application/json',
            success: function (e) {
                alert('suck');
            },
            error: function (e) {
                alert('no');
            },
        });
    });
});
