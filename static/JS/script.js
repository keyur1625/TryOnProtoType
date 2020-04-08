function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).ready(function(){
    console.log("Welcome to TryOn!");
    $("#product_category").change(function(){
        var category = $(this).val();
        // alert("Category: "+category)
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie('csrftoken') }
        });
        $.ajax({
            url: 'trial/loadproducts/',
            type: 'POST',
            data: {'category': category},
            success: function(data){
                // console.log(data)
                $("#product1").attr('src', data.image1);
                $("#product2").attr('src', data.image2);
                if(data.type == "combo"){
                    $('.comboDemo').css("display", "block")
                }
                else{
                    $('.comboDemo').css("display", "none")
                }
            }
        });
    });

    $("#uploadTrial").submit(function(e){
        e.preventDefault();
        var formdata = new FormData(this);
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie('csrftoken') }
        });
        $.ajax({
            url:'trial/uploadoutput/',
            type:'POST',
            data: formdata,
            processData:false,
            cache:false,
            contentType:false,
            success: function(data){
                console.log(data);
                $("#output").attr('src', data);
                $("#output").attr('name', data);
            }
        });
    });

    $(".productImages").click(function(){        
        var cloth_path = $(this).attr('src');
        var append_path = $("#output").attr('name');
        var category = $("#product_category").val();
        // console.log
        if($("#output").attr('src')==""){
            alert("Please Select Image for Trial First!");
            $("#outputimage").focus();
        }
        else{
            // alert("This is product image"+cloth_path);
            $.ajaxSetup({
                headers: { "X-CSRFToken": getCookie('csrftoken') }
            });
            $.ajax({
                url: 'trial/update/',
                type: 'POST',
                data: {'cloth_path': cloth_path, 'append_path': append_path, 'category': category},
                success: function(data){
                    $("#output").attr('src', data);
                }
            });
        }
    });

    $("#comboBtn").click(function(){
        var outputimage = $("#output").attr('src');
        var path1 = $("#product1").attr('src');
        var path2 = $("#product2").attr('src');
        if(outputimage==""){
            alert("Please Select Image for Trial First!");
            $("#output").focus();
        }
        else{
            $.ajax({
                url:'trial/update/',
                type:'POST',
                data:{'cloth_path':[path1, path2], 'append_path':outputimage},
                success:function(data){
                    $("#output").attr('src');
                }
            });
        }
    });
/*
    $("#login").submit(function(e){
        e.preventDefault();
        // alert("Logged In Now");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'auth/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log("data: "+data);
                window.location.href = data
            }
        });
    });

    $("#customer_register").submit(function(e){
        e.preventDefault();
        // alert("Customer Registered");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'add/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log(data);
            }
        });
    });

    $("#shipper_register").submit(function(e){
        e.preventDefault();
        // alert("Customer Registered");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'add/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log(data);
            }
        });
    });

    $("#vendor_register").submit(function(e){
        e.preventDefault();
        // alert("Customer Registered");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'add/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log(data);
            }
        });
    });

    $('#v_doc, #s_doc').change(function(){
        // alert("File Selected");
        console.log(this);
    });

    $('#v_add, #s_add').change(function(){
        // alert("File Selected");
        console.log(this);
    });
*/
});