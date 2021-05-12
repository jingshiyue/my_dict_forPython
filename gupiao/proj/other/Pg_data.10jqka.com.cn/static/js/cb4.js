//@charset "gbk";
$(function(){

    var autosearch = new autocompleteSearch();
    autosearch.init({
        clickCallback: function(code){
            window.open('http://data.10jqka.com.cn/market/lhbgg/code/'+code+'/');
        }
    });

    /*
     * 个股数据
     * */
    var ggTable = new tableAjax();
    ggTable.init({
        box: '#ggsj',
        cont: '#ggsj',
        param: {
        	code: stockcode,
        	ajax: '1',
            page: '1'
        },
        baseUrl: '/market/lhbgg'
    });

    /**
     * 明细弹框
     */
    $(document).on("click", '.tip-trigger', function() {
        var pos = $(this).position();
        var code = $(this).attr("code");
        var date = $(this).attr("date");
        var rid = $(this).attr("rid");
        $.ajax({
            type: "GET",
            async: false,
            url: "http://data.10jqka.com.cn/ifmarket/getnewlh/code/"+code+"/date/"+date+"/rid/"+rid+"/",
            context: document.body,
            success: function(data){
                $("#lhb-cjmx-dialog").html(data);
            }
        });

        $('.lhb-tipbox').show();
        $('.lhb-tipbox-mask').show();
        return false;
    });
    $(document).on('click','.lhb-tipbox-mask,.lhb-tipbox .mod-close',function(){
        $('.lhb-tipbox').hide();
        $('.lhb-tipbox-mask').hide();
    });
   /* $('.m_table').on('mouseenter', 'td', function() {
        $(this).parent('tr').addClass('hover');
    }).on('mouseleave', 'td', function() {
        $(this).parent('tr').removeClass('hover');
    });*/

    if (sbdate != '' && sbrid != '') {
    	$.ajax({
            type: "GET",
            async: false,
            url: "http://data.10jqka.com.cn/ifmarket/getnewlh/code/"+stockcode+"/date/"+sbdate+"/rid/"+sbrid+"/",
            context: document.body,
            success: function(data){
                $("#lhb-cjmx-dialog").html(data);
            }
        });

        $('.lhb-tipbox').show();
        $('.lhb-tipbox-mask').show();
        return false;
    }
});
/**
 * 行情数据
 */
function toDecimal2(x) {    
    var f = parseFloat(x);    
    if (isNaN(f)) {    
        return false;    
    }    
    var f = Math.round(x*100)/100;    
    var s = f.toString();    
    var rs = s.indexOf('.');    
    if (rs < 0) {    
        rs = s.length;    
        s += '.';    
    }    
    while (s.length <= rs + 2) {    
        s += '0';    
    }    
    return s;    
} 
var quote = function() {
	$.ajax({
		url : "http://qd.10jqka.com.cn/quote.php?return=json&cate=real&type=stock&code="+stockcode,
		type : "get",
		dataType : "jsonp",
		success : function(data){
			if (data.data) {
				var zxj = data.data[stockcode][10]?data.data[stockcode][10]:'0.00',
					zde = data.data[stockcode][264648]?toDecimal2(data.data[stockcode][264648]):'0.00',
					zdf = data.data[stockcode][199112]?toDecimal2(data.data[stockcode][199112]):'0.00',
					color = data.data[stockcode][199112]>0?'c-rise':data.data[stockcode][199112]<0?'c-fall':'',
					scolor = data.data[stockcode][199112]>0?'arr-rise':data.data[stockcode][199112]<0?'arr-fall':'',
					imcolor = data.data[stockcode][199112]>0?'icon_rise':data.data[stockcode][199112]<0?'icon_fall':'icon_equal',
					prefix = data.data[stockcode][199112]>0?'+':'';
				$(".jj_stock_trend").html('<p class="'+color+'"><span class="fz24 mr8 '+scolor+'">'+zxj+'</span>'+
						prefix+zde+'('+prefix+zdf+'%)'+'</p><p class="mt4">所属行业：<span class="c-blue">'+hy+'</span></p>');
			}
		}
	})	
}
quote();
setInterval('quote()', 20000);