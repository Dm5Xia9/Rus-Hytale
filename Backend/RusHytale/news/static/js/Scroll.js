
    $(document).scroll(function(e) {
        if($(window).scrollTop() > 5){
            $('.header').addClass('headerScroll1');

            
        }
        else{
            $('.header').removeClass('headerScroll1');
        }

        if($(window).scrollTop() > 10){
            $('.header').addClass('headerScroll2');
        }
        else{
            $('.header').removeClass('headerScroll2');
        }

        if($(window).scrollTop() > 15){
            $('.header').addClass('headerScroll3');
        }
        else{
            $('.header').removeClass('headerScroll3');
        }

        if($(window).scrollTop() > 20){
            $('.header').addClass('headerScroll4');
        }
        else{
            $('.header').removeClass('headerScroll4');
        }

        if($(window).scrollTop() > 25){
            $('.header').addClass('headerScroll5');
        }
        else{
            $('.header').removeClass('headerScroll5');
        }
    });