function login(){
    var username=$("#username").val()
    var password=$("#password").val()
    data={"username":username,"password":password}
    $.ajax({
        type:"post",
        url:"/login",
        data:JSON.stringify(data),
        cache:false,
        success:function(data){
            if(data=="true"){
                alertDiv("验证正确，登陆成功。(三秒后自动跳转)");
                setTimeout(function(){
                    window.location.reload()
                },3000)
            }else{
                alertDiv("用户名或密码错误，请重新登陆。");
            }

        },
        error:function(){
            alertDiv("error!");
        },
    });
}
function register(id){

    iframe = $("#alertFrame")
    contentWindow = iframe[0].contentWindow
    login_name = iframe.contents().find("#login_name").val()
    user_name = iframe.contents().find("#user_name").val()
    pwd = iframe.contents().find("#pwd").val()
    if (contentWindow.user_name_boo && contentWindow.login_name_boo && contentWindow.pwd_boo && contentWindow.repwd_boo) {
        data = {"login_name": login_name, "user_name": user_name, "pwd": pwd}
        $.ajax({
            type: "post",
            url: "/register",
            data: JSON.stringify(data),
            cache: false,
            success: function (data) {
                if (data=="True"){
                    alertDiv("注册成功！");
                    delCover(id)
                }else{
                    contentWindow.check_user_name()
                    contentWindow.check_login_name()
                    contentWindow.check_pwd()
                }
            },
            error: function () {
                alertDiv("error!");
            },
        });

    } else {
        contentWindow.check_user_name()
        contentWindow.check_login_name()
        contentWindow.check_pwd()
    }


}