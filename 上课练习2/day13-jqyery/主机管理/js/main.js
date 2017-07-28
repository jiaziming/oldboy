/**
 * Created by super on 2016/4/12.
 */

group = [
    {'value':'1', txt:'开发组'},
    {'value':'2', txt:'运维组'},
    {'value':'3', txt:'测试组'}
];
stat = [
    {value:'1', txt:'在线'},
    {value:'2', txt:'离线'}
];

/*左侧菜单点击显示效果*/
$(".menu").click(function () {
    $(this).parent().children(".menu-body").hide("normal");
    $(this).next(".menu-body").show("slow");
});

//单击菜单1
$("#menu-1-1").click(function () {
    $(".content").show();
    $(".readme").hide();
});
$("#menu-1-2").click(function () {
    $(".content").hide();
    $(".readme").show();
});

/*鼠标指向行改变颜色方法
$("table tr ").mouseover(function () {
    $(this).addClass("tr_hover");
});

$("table tr ").mouseout(function () {
    $(this).removeClass("tr_hover");
});  */

/* 全选 /取消功能 */
function selectAll() {
    //如果有选中的记录就保存
    if ($("#editstatus").attr("status") == "true") {
        $(".chk_id").each(function () {
            var editlist = $(this).parent().nextAll();
            if ($(this).prop("checked")) {
                trToViewModule(editlist);
                $(this).removeAttr("checked");
            } else {
                $(this).prop("checked", true);
                trToEditModule(editlist);

            }
        });
        //获取当前还有没有选中的
        var chk_num = 0;
        $(".chk_id").each(function () {
            if ($(this).prop("checked")) {
                chk_num += 1;
            }
        });
        //如果没有选中的就初始化
        if (chk_num == 0) {
            backInitStatus();
        }
        
    } else {
        $(".chk_id").each(function () {
            if ($(this).prop("checked")) {
                $(this).removeAttr("checked");
            } else {
                $(this).prop("checked", true);
            }
        });
    }
}

/*单行编辑*/
function editCurrTr(ths) {
    var result = {}; //定义一个对象
    var editlist = $(ths).parent().prevAll(); //获取当前行的所有td对象
    
    // 获取需要编辑的td及值
    $(editlist).each(function () {
        if ($(this).attr('edit')=='1'){
            var key = $(this).attr('col');
            var vals  = $(this).text();
            result[key] = vals;
        }
    });

    //console.log(result)
    // 显示遮罩图层
    $("#show_bg").css({'display':'block'});
    $(".show").css({
        'display':'block',
        'left':($("body").width()/2 - $(".show").width()/2)+'px',
        'top':($(document).height()/2 - $(".show").height()/2)-30+'px'
    });

    //填充值
    $("#host").val(result.host);
    $("#ip").val(result.ip);
    $("#cpu").val(result.cpu);
    $("#disk").val(result.disk);
    $("#mem").val(result.mem);

    //填充两个select
    var tmpa = ['group','stat'];
    for(var i in tmpa){
        //获取定义变量的对象内容
        var def_content = window[tmpa[i]];
        console.log(def_content);
        var optionstr = "";
        $(def_content).each(function () {
           //console.log($(this).attr('value'));
           if (($(this).attr('txt') == result.group )||($(this).attr('txt') == result.stat )) {
               optionstr += "<option value='" + $(this).attr('value') + "' selected>" + $(this).attr('txt') + "</option>";
           }else{
               optionstr += "<option value='" + $(this).attr('value') + "' >" + $(this).attr('txt') + "</option>";
           }
        });
        optionstr = "<select class='edit-input'>"+optionstr+"</select>";
        console.log(optionstr);
    $("#"+tmpa[i]).html(optionstr);
    }

}

/*关闭遮罩层*/
function hideShow() {
    $(".show").css({'display':'none'});
    $("#show_bg").css({'display':'none'});
}

//错误消息提示
function alertMsg(message) {
    $("#err-msg").text(message);
    $("#err-msg").css('display','block');

    var t = setTimeout('$("#err-msg").css("display","none")',1500);
}

/*将选中的所有行的指定列进入编辑模式*/
function editAllTr() {
    var checked_num = 0;
    //如果已经是编辑模式就不能再点击了编辑了
    if ($("#editstatus").attr("status") == "true"){
        alertMsg('当前已经是编辑模式');
        return false;
        }

    // 遍历所有的checkbox，对选中的进行操作
    $(".chk_id").each(function () {
        if ($(this).prop('checked')){
            //若改行已经选中，找它后面的所有兄弟td标签
            var editlist = $(this).parent().nextAll();
            trToEditModule(editlist);
            checked_num += 1;
        }
    });

    //如果未找到选中的记录则无法进入编辑模式
    if (checked_num == 0){
        alertMsg('请选择要编辑的记录!');
        return false;
    }else{
        //设置编辑状态为true
        $("#editstatus").attr("status",true);
        //改变颜色
        $("#a-edit").css({'background':'lawngreen'});
        $("#a-save").css({'background':'lawngreen'});
    }
}

/*保存修改*/
function saveAllTr() {
    //如果当前不是编辑模式就什么也不做
    if ($("#editstatus").attr("status") == "false"){
        alertMsg("编辑模式未启用!");
        return false;
    }else{
    //如果是编辑模式
    $(".chk_id").each(function () {
        if ($(this).prop('checked')) {
            //若改行已经选中，找它后面的所有兄弟td标签
            var editlist = $(this).parent().nextAll();
            //改为view模式
            trToViewModule(editlist);
            //修改完将选中的标签取消
            $(this).removeAttr("checked");
        };
    });

    backInitStatus();
    }
    alertMsg('修改成功!');
}

// 取消编辑模式并恢复初始状态
function backInitStatus() {
    //保存完成后将编辑按钮的颜色恢复
    $("#a-edit").css({'background':'#ffffff'});
    $("#a-save").css({'background':'#ffffff'});
    //将编辑模式置为初始状态
    $("#editstatus").attr("status",false);
    //全选chkbox取消选中
    $("#checkall").removeAttr("checked");
}

//将tr转换为编辑模式函数
function trToEditModule(editlist) {
    //editlist为当前行要编辑的列表对象
    $(editlist).each(function () {
        if ($(this).attr('edit') =='1'){
           var td_value = $(this).text(); //获取td的text值

           //判断是否是替换成select标签
           if ($(this).attr('isselect') == '1'){
               //填充为select标签
               var select_name = $(this).attr('col');
               var select_content = window[select_name];
               var optionstr = "";
               $(select_content).each(function () {
                   //console.log($(this).attr('value'));
                   if($(this).attr('txt') == td_value) {
                       optionstr += "<option value='" + $(this).attr('value') + "' selected>" + $(this).attr('txt') + "</option>";
                   }else{
                       optionstr += "<option value='" + $(this).attr('value') + "' >" + $(this).attr('txt') + "</option>";
                   }
               });
               optionstr = "<select class='edit-input'>"+optionstr+"</select>";
               $(this).html(optionstr);

           }else {
               //替换为input标签
               $(this).html("<input type='text' class='edit-input' value='" + td_value + "'/>");
           }
       }
    });
}

//将当前行由编辑模式变为浏览模式
function trToViewModule(editlist) {
    //开始遍历所有标签
    $(editlist).each(function () {
        //如果td的edit标识为1标识该td需要修改，获取值
        if ($(this).attr('edit') == '1') {
            //如果是select标签获取text值
            if ($(this).attr('isselect') == '1'){
               //console.log($(this).children(":first").children(":selected"));
                var td_value = $(this).children(":first").children(":selected").text();

            }else {
                var td_value = $(this).children(":first").val();
            }
            $(this).html(td_value);
        }
    });
}


/* 单独点击每个checkbox框时触发事件 */
function chkChoose(ths) {
    //点击选中
    if ($(ths).prop("checked")) {
        //当前是否是编辑状态，如果是就将选中的行业进入编辑模式
        if ($("#editstatus").attr("status") == "true"){
            var editlist = $(ths).parent().nextAll();
            trToEditModule(editlist)
        }
    }else{
        //点击取消选中,如果当前未编辑模式就取消编辑模式，修改值为input值
        if ($("#editstatus").attr("status") == "true"){
            var editlist = $(ths).parent().nextAll();

            //改为view模式
            trToViewModule(editlist);
        }

        //判断当前是否还有进入编辑模式的td,如果没有了就将进入编辑模式和保存修改按钮初始化
            var chk_num = 0;
            $(".chk_id").each(function () {
                if ($(this).prop("checked")){
                    chk_num += 1;
                }
            });
            console.log("current checked num:"+chk_num);
            //如果有什么都不做
            if (chk_num > 0){
                return false;
            }else{
                //没有了，初始化编辑模式和保存状态按钮
                //保存完成后将编辑按钮的颜色恢复
                backInitStatus();
            }
    }
}