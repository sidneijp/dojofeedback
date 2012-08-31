$('.form_novo').on('submit', function() {

    $.post('dojo/create/', {name: $('input[name]').val().toLowerCase()}, function(data){
        if(data.success){
            var comment = data.dojo_link;
            var feedback = data.feedback_link;
            var comment_link = $('.links:eq(0)').html().match(/.*\/a\>/)[0];
            var feedback_link = $('.links:eq(1)').html().match(/.*\/a\>/)[0];

            $('.links:eq(0)').html(comment_link + comment);
            $('.links:eq(0)').find('a').attr("href", comment);
            $('.links:eq(1)').html(feedback_link + feedback);
            $('.links:eq(1)').find('a').attr("href", feedback);
            $('.menu_progresso').attr('class', 'menu_progresso menu_progresso_2');
            $('div#errors_flash_messages').html('');

            $('#qrcode').find('img').attr('src', comment + '.qrcode');
            //$('#qrcode').css('display', 'block');
        }
        else{
            $('div#errors_flash_messages').html('');
            var i;
            for (i in data.errors)
                $('div#errors_flash_messages').append(data.errors[i]+'<br>');
        }

    });
    return false;
});


$('.comentarios_feed').append('<p class="mensagem">Clique para exibir</p>');
$('.comentarios_feed').addClass("esconder_comentarios").click(function(){
    $(this).toggleClass("esconder_comentarios");
    $(this).find('.mensagem').toggleClass("esconder_mensagem");
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
