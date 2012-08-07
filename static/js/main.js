$('.form_novo').on('submit', function() {

    $.post('dojo/create', {name: $('input[name]').val().toLowerCase()}, function(data){
        if(data.success){
            
            host = window.location.href.replace("#","");
            data.dojo_link = String(data.dojo_link).replace("/","");
            data.feedback_link = String(data.feedback_link).replace("/","");
            
            var comment = host+data.dojo_link;
            var feedback = host+data.feedback_link;

            $('.links:eq(0)').append(comment);
            $('.links:eq(0)').find('a').attr("href", comment);
            $('.links:eq(1)').append(feedback);
            $('.links:eq(1)').find('a').attr("href", feedback);
        }
        else{
            alert("Dojo já existe.")
        }

    });
    return false;
});


$('.comentarios_feed').append('<p class="mensagem">Clique para exibir</p>');
$('.comentarios_feed').addClass("esconder_comentarios").click(function(){
    $(this).toggleClass("esconder_comentarios")
    $(this).find('.mensagem').toggleClass("esconder_mensagem")
});


$(document).ready(function() {
    $('.submit').click(function(){
        if($(this).attr("title") == "positivo"){
            $('#status').attr("value", "1");    
        }
        else{
            $('#status').attr("value", "2");
        }
        $('#comment_form').submit();
    });
});