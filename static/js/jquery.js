$('input').bind('keyup',function(event){
    var maxlen = $(this).attr('maxlength');
    if($(this).val().length >= parseInt(maxlen))
    {
        var next = $(this).next();
        if(next)
            next.focus();
    }
});