$(document).ready(function(){
    $('.m_menu').click(function(){
      $('.menu-hide').toggleClass('show');
      $('.m_menu').toggleClass('active');
      if($('.center_panel_content_main').attr('style') == 'display:none'){
        $('.center_panel_content_main').attr('style', 'display:block');
      }
      else{
        $('.center_panel_content_main').attr('style', 'display:none');
      }

    });
    $('a').click(function(){
      $('.menu-hide').removeClass('show');
      $('.m_menu').removeClass('active');

    });
  });


