$('.dropdown-item').('click',  (function(){
        var btnObj = $(this).parent().siblings('button');
        $(btnObj).text($(this).text());
        $(btnObj).val($(this).text());
    }));