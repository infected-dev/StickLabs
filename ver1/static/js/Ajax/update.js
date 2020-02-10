$('#addDesignModal' ).on('shown.bs.modal', function(){
    $('#designo').focus()
})

$('#addDesignModalSubmit').on('click', function(){
    var t = $('#designo').val()
    var j = $('#designame').val()

    req = $.ajax({
        url : '/addNewDesign',
        type : 'POST',
        data : {d_no : t, d_name:j},
        success: function(data){
            var d = "<tr><td>"+ data.d_no +"</td><td>"+data.d_name+"</td><td>"+data.d_date+"</td></tr>"
            table = $('#designTable tbody')
            table.append(d)
        }
    });

    
    $('#addDesignModal').modal('toggle')

});

