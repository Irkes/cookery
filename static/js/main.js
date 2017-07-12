/**
 * Created by eireen on 28.5.17.
 */
$('button').on('click', function(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url:'/like/',
        type: 'GET',
        data :{ recipe_id : element.attr("data_id")} ,
        success : function(response){
            element.html(' ' + response);
        }

    });
}
);