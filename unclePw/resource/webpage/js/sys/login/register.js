var user_name_boo=false;
var login_name_boo=false;
var pwd_boo=false;
var repwd_boo=false;

function check_user_name() {
    user_name=$("#user_name").val()
    length=user_name.length
    if (length>18 || length<6){
        $("#user_name_td").html("昵称长度必须在6-18位之间！")
        $("#user_name_td").css("color","red")
        user_name_boo=false
        return false
    }else{
        $("#user_name_td").html("昵称可以使用！")
        $("#user_name_td").css("color","green")
        user_name_boo=true
        return true
    }

}

function check_login_name(){
    login_name=$("#login_name").val()
    reg=/^[a-zA-Z][a-zA-Z0-9_]{4,15}$/
    if (reg.test(login_name)){
        data={"method_num":"1","user_name":login_name}
        $.ajax({
            type:"post",
            url:"/registerCheck",
            data:JSON.stringify(data),
            cache:false,
            success:function(data){
                if (data=="True"){
                    $("#login_name_td").html("登录名可以使用！")
                    $("#login_name_td").css("color","green")
                    login_name_boo=true
                    return true
                }else{
                    $("#login_name_td").html("登录名重复！请重新输入")
                    $("#login_name_td").css("color","red")
                    login_name_boo=false
                    return false
                }
            },
            error:function(){
                $("#login_name_td").html("系统出错，清及时反馈！")
                $("#login_name_td").css("color","red")
                login_name_boo=false
                return false
            },
        });
    }else{
        $("#login_name_td").html("必须以字母开头的是5-16位字符，可包括下划线_")
        $("#login_name_td").css("color","red")
        login_name_boo=false
        return false
    }
}

function check_pwd(){
    pwd=$("#pwd").val()
    reg=/^[a-zA-Z0-9]{6,16}$/
    if (reg.test(pwd)){
        $("#pwd_td").html("密码可以使用！")
        $("#pwd_td").css("color","green")
        pwd_boo=true
        return check_repwd()
    }else{
        $("#pwd_td").html("密码必须为6-16位的字母或数字！")
        $("#pwd_td").css("color","red")
        pwd_boo=false
        return false
    }
}

function check_repwd(){
    pwd=$("#pwd").val()
    repwd=$("#repwd").val()
    if (pwd==repwd){
        $("#repwd_td").html("输入正确！")
        $("#repwd_td").css("color","green")
        repwd_boo=true
        return true
    }else{
        $("#repwd_td").html("密码不一致，请重新输入！")
        $("#repwd_td").css("color","red")
        repwd_boo=false
        return false
    }
}