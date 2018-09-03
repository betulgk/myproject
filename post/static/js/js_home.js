$(document).ready(function(){
        console.log("on ready...");
        console.log("tt");
        window.alert(gettext('this is to be translated'));
        // document.write(gettext('this is to be translated'));
        // var object_cnt = 1
        // s = ngettext('literal for the singular case',
        // 'literal for the plural case', object_cnt);
        // fmts = ngettext('There is %s object. Remaining: %s',
        //    'There are %s objects. Remaining: %s', 11);
        // s = interpolate(fmts, [11, 20]);

        function getCookie(c_name)
            {
                var c_end, c_start;
                if (document.cookie.length > 0) {
                    c_start = document.cookie.indexOf(c_name + "=");
                    if (c_start != -1) {
                        c_start = c_start + c_name.length + 1;
                        c_end = document.cookie.indexOf(";", c_start);
                        if (c_end == -1) c_end = document.cookie.length;
                        return unescape(document.cookie.substring(c_start, c_end));
                    }
                }
            return "";
            }

            $('#btnsubmit').click(function(e){
            e.preventDefault();
            console.log($('#post_name').val());
            console.log($('#post_content').val());
            var name = $('#post_name').val();
            var contents = $('#post_content').val();

            if (name.length == 0 && contents.length == 0){
                swal("Oups!", "Post name and Post content are required!", "error");
                return;
            }
            else if (name.length == 0 ) {
                swal("Oups!", "Post name is required!", "error");
                return;
            }
            else if (contents.length == 0) {
                swal("Oups!", "Post content is required!", "error");
                return;
            }
            else{
                swal("Post Name : " + name , "Post Content : " + contents , "success");
            }

            var user = $("#user-username").text();
            console.log("yeee", user);
            console.log(user);
            $.ajax({
                url: 'newestposts/51',
                data: {'post_name' : name,
                        'post_content':contents},
                type : 'POST',
                dataType:'json',
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                success: function(data) {
                    console.log(data);
                    $('#myModal').modal('toggle');

                    if(data['saved']=='True'){
                        var html='<br><div class="container_post1">\
                        <div class="post_id" style="display:none;">{{post.id}}</div> \
                        <div class ="create_post">\
                        <div class="personal_info">\
                        <div class="photo_line"></div>\
                            <img class="pp" src="pp.png">\
                            <p id="name_post"><b> Post name : </b>  '+name+'</p>\
                            <p><b>By : '+user+'</b></p>\
                        </div>\
                        <hr class="h_line" color="black">\
                        <div class="outer">\
                        <div class="v_line"></div>\
                        </div>\
                        <p class="content">\
                        <b>Content :</b> '+contents+' </p>\
                        </div>\
                        </div>';
                    $( ".middle" ).prepend(html);
                    }
                   }
                })
            });
    });