$(document).ready(function(){
    $('.m_menu').click(function(){
      $('.menu-hide').toggleClass('show');
      $('.m_menu').toggleClass('active');
    });
    $('a').click(function(){
      $('.menu-hide').removeClass('show');
      $('.m_menu').removeClass('active');
    });
  });



  $( document ).ready(function() {
    $('.text_read_mess').click(function(){
        var num_ar = $('.article_block_s').length;
        $('.text_read_mess').removeClass('read_mess_active');
        $.ajax({
        type:"POST",
        url: "/articles/",
        data: {num_articles: num_ar},
        success: function(data) {
          var data = JSON.parse(data);
          $(".center_panel_content_main").append(
            "<div class='user_wall_profile'>"+
            "<img src='{{post.user_post.avatar.url}}' class='ava_user_wall_profile' style='border-radius: 5px;border:none;'>"+
            "<div class='username_user_wall_profile'>{{post.user_post.username}}</div>"+
            "<div class='date_user_wall_profile'>2020.02.03</div>"+
            "</div>"+
            "<div class='content_wall_profile'>"+
            "<div class='text_content_wall_profile'>"+
            
            "</div>"+
            "</div>"
          );
        }
      })
    })
  })