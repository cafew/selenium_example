//弹出框，包括信息text，以及一个确认按钮
function alertDiv(text){
    //生成一个随机id
    var time=new Date().getMilliseconds()
    var num=Math.ceil(Math.random()*10000)
    var id=time+""+num
    //设置完全屏蔽的div
    width=document.body.offsetWidth+"px"
    height=document.body.offsetHeight+"px"
    //alert(width+"-"+height)
    var div_html="<div id='cover"+id+"' style='position: absolute;top: 0px;left: 0px;width:"+width+";height:"+height+";'></div>"
    $("body").append(div_html)
    //设置弹出框
    width2=Math.max(document.body.offsetWidth*0.2,300)+"px"
    height2=Math.max(document.body.offsetHeight*0.2,90)+"px"
    left2=document.body.offsetWidth*0.22+"px"
    top2=document.body.offsetHeight*0.1+"px"
    top2_begin=document.body.offsetHeight*0.3+"px"
    var div2_html="<div id='alert"+id+"' class='shadow alert' style='top:"+top2_begin+";left:"+left2+";width:"+width2+";height:"+height2+";'></div>"
    $("body").append(div2_html)
    //设置弹出框显示内容
    height3=document.body.offsetHeight*0.2*0.6+"px"
    var content_html="<div style='background-color: white;height:"+height3+"'>"+text+"</div>"
    $("#alert"+id).append(content_html)
    //设置弹出框的确定按钮
    width3=document.body.offsetWidth*0.2*0.5+"px"
    var button_html="<button onclick=\"delCover('"+id+"')\" style='margin-top:15px;width:"+width3+"'>确定</button>"
    $("#alert"+id).append(button_html);
    //从下渐出
    $("#alert"+id).animate({
        top:top2,
        opacity:'1'
    })
}
//关闭刚才的弹出框
function delCover(id){
    $("#alert"+id).animate({
        top:'200px',
        opacity:'0'
    })
    $('#cover'+id).remove()
    setTimeout(function(){
        $('#alert'+id).remove()
    },300)

}
//弹出框，包括一个iFrame，路径为参数
function alertFrame(path,bu1_name,bu2_name,fun_name){
    //生成一个随机id
    var time=new Date().getMilliseconds()
    var num=Math.ceil(Math.random()*10000)
    var id=time+""+num
    //设置完全屏蔽的div
    width=document.body.offsetWidth+"px"
    height=document.body.offsetHeight+"px"
    //alert(width+"-"+height)
    var div_html="<div id='cover"+id+"' style='position: absolute;top: 0px;left: 0px;width:"+width+";height:"+height+";'></div>"
    $("body").append(div_html)
    //设置弹出框
    width2=document.body.offsetWidth*0.4+"px"
    height2=document.body.offsetHeight*1.2+"px"
    left2=document.body.offsetWidth*0.11+"px"
    top2=document.body.offsetHeight*0.1+"px"
    top2_begin=document.body.offsetHeight*0.3+"px"
    var div2_html="<div id='alert"+id+"' class='shadow alert' style='top:"+top2_begin+";left:"+left2+";width:"+width2+";height:"+height2+";'></div>"
    $("body").append(div2_html)

    //设置弹出框显示内容
    height3=document.body.offsetHeight*1.2*0.90+"px"
    width3=document.body.offsetWidth*0.4+"px"
    var content_html="<iframe src='"+path+"' id='alertFrame' width='"+width3+"' style='background-color: white;height:"+height3+";'>"+path+"</iframe>"
    $("#alert"+id).append(content_html)
    //设置弹出框的确定按钮
    width3=document.body.offsetWidth*0.2*0.5+"px"
    var button_html="<button onclick=\"delCover('"+id+"')\" style='margin-top:15px;margin-left:10px;width:"+width3+"'>"+bu1_name+"</button>"
    button_html += "<button onclick=\"" + fun_name + "('" + id + "')\" style='margin-top:15px;margin-left:150px;width:" + width3 + ";'>" + bu2_name + "</button>"
    $("#alert"+id).append(button_html)
    //从下渐出
    $("#alert"+id).animate({
        top:top2,
        opacity:'1'
    })
}