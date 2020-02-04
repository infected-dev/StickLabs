$(document).ready(function(){
    $('.vupdateout').keydown(function (e){
        var id =  $(this).attr('attribute')
         if(e.keyCode == 13){
              $('#button'+id).click()   
         }
     })
})


$(document).ready(function(){
    $('.vupdateoutout').keydown(function (e){
        var id =  $(this).attr('attribute')
        if(e.keyCode == 13){
            $('#button'+id).click()
        }
     })
})

$(document).ready(function(){
    $('.vupdatemillin').keydown(function (e){
        var id =  $(this).attr('attribute')
        if(e.keyCode == 13){
            $('#button'+id).click()
        }
     })
})

$(document).ready(function(){
    $('.vupdatein').keydown(function (e){
        var id =  $(this).attr('attribute')
        if(e.keyCode == 13){
            $('#button'+id).click()
        }
     })
})


$(document).ready(function(){
   
        $('.update').on('click', function(){
            var id = $(this).attr('attributes');
    
           var exit_time = $('#exittime'+id).val()
           var entrytime = $('#entrytime'+id).val()
           //alert(exittime);
    
           req = $.ajax({
               url : '/visitors/update',
               type : 'POST',
               data : {vi_id : id , exittime:exit_time, entrytime:entrytime}
           });
    
           $('#datasection'+id).fadeOut(1000).fadeIn(1000);
        });

});

$(document).ready(function(){
    $('.updateagency').on('click', function(){
        var id = $(this).attr('attributes')
        var out_time = $('#outtimea'+id).val()

        req = $.ajax({
            url : '/updateAgency',
            type : 'POST',
            data : {lid : id, exitime:out_time}
        });

        $('#data'+id).fadeOut(1000).fadeIn(1000);

    });
});

$(document).ready(function(){

    $('.updatevehicles').on('click', function(){
        
        var id = $(this).attr('attributes');
    
       var out_time = $('#outtime'+id).val()
        var in_time = $('#intime'+id).val()
       //alert(out_time);
       req = $.ajax({
        url : '/vehicles/update',
        type : 'POST',
        data : {VeID : id ,intime:in_time, outtime:out_time}
        });

        $('#datasectionveh'+id).fadeOut(1000).fadeIn(1000);

    });
       
});

$(document).ready(function(){

    $('.updatemill').on('click', function(){
        
        var id = $(this).attr('attributes');
    
       var in_time = $('#intime'+id).val()
    
       req = $.ajax({
        url : '/vehicles/mill/update',
        type : 'POST',
        data : {vid : id , intime:in_time}
        }); 

        $('#datasectionmill'+id).fadeOut(1000).fadeIn(1000);

    });
       
});

function newFunction() {
    return $();
}
