//@charset "utf-8";
/**
 * 键盘精灵
 * author: huaxiaolong
 * date: 2012-05-16 13:07
 * update : 2017-05-10
 * author: luhuiyue
 * 修复搜索框无法通过“放大镜”按钮和回车键进行搜索Bug
 */
(function ($) {
    $.format = function (source, params) {
        if (arguments.length == 1) return function () {
            var args = $.makeArray(arguments);
            args.unshift(source);
            return $.format.apply(this, args);
        };
        if (arguments.length > 2 && params.constructor != Array) {
            params = $.makeArray(arguments).slice(1);
        }
        if (params.constructor != Array) {
            params = [params];
        }
        $.each(params, function (i, n) {
            source = source.replace(new RegExp("\\{" + i + "\\}", "g"), n);
        });
        return source;
    };
    $.fn.autocomplete = function (options) {
        var opt = {
            isSpeech: false,
            container: [],
            data: [],
            valueList: [],
            boxList: [],
            type: 0,
            extra: true,
            text: null,
            count: '5_1',
            index: 0,
            input: null,
            SearchBtn: '.search-btn',
            window: 'new',
            urlPattern: null,
            displaycode: true
        };
        var typeList = ['fund', 'stock', 'company', 'field', 'concept', 'area', 'hk', 'yyb'];
        var typeInfo = {
            'fund': {
                name: '\u57FA\u91D1',
                mark: 0
            },
            'stock': {
                name: '\u80A1\u7968',
                mark: 1
            },
            'company': {
                name: '\u57FA\u91D1\u516C\u53F8',
                mark: 2
            },
            'field': {
                name: '\u884C\u4E1A',
                mark: 3
            },
            'concept': {
                name: '\u6982\u5FF5',
                mark: 4
            },
            'area': {
                name: '\u5730\u57DF',
                mark: 5
            },
            'hk': {
                name: '\u6E2F\u80A1',
                mark: 6
            },
            'yyb': {
                name: '\u8425\u4E1A\u90E8',
                mark: 7
            }
        };
        var prefix = 'autocomplete';

        var init = function (self) {
            var defaultType = {
                stock: true,
                hk: true,
                fund: true
            };
            for (var a in options) {
                if (options[a] != null) {
                    if (typeInfo[a]) {
                        defaultType[a] = options[a];
                    } else {
                        opt[a] = options[a]
                    }
                }
            }
            if (defaultType['stock'] && defaultType['fund']) {
                opt.type = 0;
            } else if (defaultType['stock'] && defaultType['hk']) {
                opt.type = 1;
            } else {
                for (var a in defaultType) {
                    if (defaultType[a]) {
                        opt.type = a;
                        break
                    }
                }
            }
            opt.input = self;
            $("#" + prefix + "_" + self.id).remove();
            opt.container[self.id] = $("<div>").addClass("autocomplete").attr("id", prefix + "_" + self.id).hide().css({
                "z-index": parseInt(new Date().getTime() / 1000),
                "position": "absolute"
            }).appendTo($("body"));
            $(self).attr("autocomplete", "off");
            var $container = opt.container[self.id];
            if (opt.width) {
                $container.width(opt.width);
            } else {
                $container.outerWidth(Math.max($container.width("").outerWidth() + 1, $(self).outerWidth()));
            }
            if (opt.func) {
                $.each(opt.func, function (i, func) {
                    if (typeof(func) == 'object') {
                        func.bindFunc($container, self)
                    }
                })
            }
            if (self.webkitSpeech != undefined) {
                opt.isSpeech = true
            }
        };

        var clean = function () {
            var self = opt.input;
            opt.container[self.id].hide();
        };

        var setIndex = function (index) {
            var self = opt.input;
            var $div = opt.container[self.id];
            var total = $div.find('dd').size() + $div.find('dt').size();
            if (index < 1 || index > total) {
                return;
            }
            opt.index = index;
            var $target = $div.find(".auto-item[did='" + index + "']");
            $div.find('dd,dt').removeClass('selected');
            $target.addClass('selected');
            $div.show();
        };

        var talog = function () {
            if (opt.statid && window.TA) {
                TA.log({
                    id: opt.statid,
                    nj: 1,
                    _sid: 'img_' + opt.statid
                });
            }
        };

        var redirect = function (url) {
            if (opt.window == 'self') {
                window.location.href = url
            }
            if (opt.window == 'new') {
                window.open(url)
            }
        };

        var submit = function () {
            var
                text = opt.text,
                encodeText = encodeURIComponent(text),
                self = opt.input,
                index = opt.index,
                defaultText = self.defaultValue,
                $div = opt.container[self.id];
            talog();
            if (!opt.stype || !opt.scode) {
                //瑙ｆ瀽index
                var $target = $div.find(".auto-item[did='" + index + "']");
                if ($target[0]) {
                    opt.stype = $target.parent().attr('data-type');
                    if ($target[0].nodeName.toUpperCase() == 'DD') {
                        opt.scode = $target.attr('data-code');
                        opt.spy = $target.attr('data-py');
                    }
                }
            }
            if (opt.clickFunc) {
                $.each(opt.clickFunc, function (i, func) {
                    if (typeof(func) == 'object' && opt.scode) {
                        func.run(opt.scode, opt)
                    }
                })
                return
            }
            if (text == '' || text == defaultText) {
                redirect('http://search.10jqka.com.cn');
                return
            }
            if (!opt.stype) {
                return
            }
            switch (opt.stype) {
                case 'blog' :
                    redirect("http://search.10jqka.com.cn/search?tid=blog&qs=box_ths&w=" + encodeText);
                    break;
                case 'forum' :
                    redirect("http://search.10jqka.com.cn/search?tid=forum&qs=box_ths&w=" + encodeText);
                    break;
                case 'news' :
                    redirect("http://search.10jqka.com.cn/search?tid=news&qs=box_ths&w=" + encodeText);
                    break;
                case 'stock' :
                    if (opt.scode) {
                        var url = "http://stockpage.10jqka.com.cn/" + opt.scode + "/";
                        if (opt.urlPattern && opt.urlPattern['stock']) {
                            url = $.format(opt.urlPattern['stock'], opt.scode)
                        }
                        redirect(url)
                    }
                    break;
                case 'fund' :
                    if (opt.scode) {
                        var url = "http://fund.10jqka.com.cn/" + opt.scode + "/";
                        if (opt.urlPattern && opt.urlPattern['fund']) {
                            url = $.format(opt.urlPattern['fund'], opt.scode)
                        }
                        redirect(url)
                    }
                    break;
                case 'hk' :
                    if (opt.scode) {
                        var url = "http://stockpage.10jqka.com.cn/HK" + opt.scode.substr(2, 4) + "/";
                        if (opt.urlPattern && opt.urlPattern['hk']) {
                            url = $.format(opt.urlPattern['hk'], opt.scode)
                        }
                        redirect(url)
                    }
                    break;
                case 'company' :
                    if (opt.scode) {
                        var url = "http://fund.10jqka.com.cn/company/" + opt.scode + "/";
                        if (opt.urlPattern && opt.urlPattern['company']) {
                            url = $.format(opt.urlPattern['company'], opt.scode)
                        }
                        redirect(url)
                    }
                    break;
                case 'field' :
                    if (opt.spy) {
                        var url = "http://q.10jqka.com.cn/stock/thshy/" + opt.spy + "/";
                        if (opt.urlPattern && opt.urlPattern['field']) {
                            url = $.format(opt.urlPattern['field'], opt.spy)
                        }
                        redirect(url)
                    }
                    break;
                case 'concept' :
                    if (opt.spy) {
                        var url = "http://q.10jqka.com.cn/stock/gn/" + opt.spy + "/";
                        if (opt.urlPattern && opt.urlPattern['concept']) {
                            url = $.format(opt.urlPattern['concept'], opt.spy)
                        }
                        redirect(url)
                    }
                    break;
                case 'area' :
                    if (opt.spy) {
                        var url = "http://q.10jqka.com.cn/stock/dy/" + opt.spy + "/";
                        if (opt.urlPattern && opt.urlPattern['area']) {
                            url = $.format(opt.urlPattern['area'], opt.spy)
                        }
                        redirect(url)
                    }
                    break;
                default:
                    break;
            }
            opt.stype = null;
            opt.scode = null;
            opt.spy = null;
        };

        var enter = function () {
            var self = opt.input,
                $div = opt.container[self.id],
                $target = $div.find('dd.selected').eq(0);
            opt.stype = $target.parent().attr('data-type');
            opt.scode = null;
            opt.spy = null;
            if ($target[0]) {
                if ($target[0].nodeName.toUpperCase() == 'DD') {
                    opt.scode = $target.attr('data-code');
                    opt.spy = $target.attr('data-py');
                }
            }
            submit()
        };

        var bindEvent = function () {
            var self = opt.input,
                $div = opt.container[self.id];
            $(opt.SearchBtn).off('click').on('click', function () {
                enter();
            })
            $div.find('.auto-item').each(function (index, el) {
                $(this).attr('did', index + 1);
            });
            $div.find('dd').each(function (index, el) {
                $(this).mouseover(function (event) {
                    $div.find('dd,dt').removeClass('selected');
                    $(this).addClass('selected')
                });
            });
            $div.find('dt').each(function (index, el) {
                $(this).mouseover(function (event) {
                    $div.find('dd,dt').removeClass('selected');
                    $(this).addClass('selected')
                });
            });
            $div.find('dd,dt').each(function (index, el) {
                $(this).click(function (event) {
                    opt.stype = $(event.target).parent().attr('data-type');
                    opt.scode = null;
                    opt.spy = null;
                    if (event.target.nodeName.toUpperCase() == 'DD') {
                        opt.scode = $(event.target).attr('data-code');
                        opt.spy = $(event.target).attr('data-py');
                    }
                    submit()
                });
            });
        };

        var render = function (data) {
            var self = opt.input,
                type = opt.type,
                $div = opt.container[self.id],
                $box = [];
            if (!type) {
                $box['stock'] = $("<dl data-type='stock'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173" + typeInfo['stock'].name + "</dt></dl>");
                $box['hk'] = $("<dl data-type='hk'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173" + typeInfo['hk'].name + "</dt></dl>");
                $box['fund'] = $("<dl data-type='fund'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173" + typeInfo['fund'].name + "</dt></dl>");
            } else if (type == 1) {
                $box['stock'] = $("<dl data-type='stock'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173" + typeInfo['stock'].name + "</dt></dl>");
                $box['hk'] = $("<dl data-type='hk'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173" + typeInfo['hk'].name + "</dt></dl>");
            } else {
                $box[type] = $("<dl data-type='" + type + "'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173" + typeInfo[type].name + "</dt></dl>");
            }
            $.each(data, function (key, item) {
                if (item.py) {
                    $("<dd class='auto-item' data-code='" + item.code + "' data-py='" + (type === 'yyb' && item.id ? item.id : item.py)
                        + "'></dd>").append("<span>" + (opt.displaycode ? item.code : '') + "</span>" + item.name).appendTo($box[type]);
                } else {
                    $("<dd class='auto-item' data-code='" + item.code + "'></dd>").append("<span>" + (opt.displaycode ? item.code : '') + "</span>" + item.name).appendTo($box[type]);
                }
            });
            $div.empty();
            for (a in $box) {
                $div.append($box[a])
            }
            if (opt.extra) {
                $("<dl data-type='news'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173\u65B0\u95FB&gt;&gt;</dt></dl>").appendTo($div);
                $("<dl data-type='forum'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173\u8BBA\u575B&gt;&gt;</dt></dl>").appendTo($div);
                $("<dl data-type='blog'><dt class='auto-item'>\u641C\"<strong></strong>\"\u76F8\u5173\u535A\u5BA2&gt;&gt;</dt></dl>").appendTo($div)
            }
            $div.find('strong').each(function () {
                $(this).html(opt.text)
            });
            bindEvent();
            setIndex(2)
        };

        var show = function (str) {
            var self = opt.input;
            var newtype = opt.type;
            opt.data = [];
            if (str) {
                opt.text = str;
            }
            if (opt.isSpeech) {
                opt.text = self.value
            }
            if (opt.valueList[opt.text]) {
                render(opt.valueList[opt.text])
            } else {
                if (opt.type == 1) {
                    newtype = 0;
                }
                if (opt.text == self.defaultValue) {
                    return;
                }
                $.ajax({
                    url: 'http://news.10jqka.com.cn/public/index_keyboard_' + encodeURIComponent($.trim(opt.text)) + '_' + newtype + '_' + opt.count + '_jsonp.html',
                    type: 'GET',
                    dataType: 'jsonp',
                    jsonpCallback: 'jsonp',
                    jsonp: false,
                    cache: true
                }).done(function (json) {
                    var nodata = [{
                        code: '',
                        name: '\u641c\u7d22\u7ed3\u679c\u4e0d\u5b58\u5728',
                        mkt: ''
                    }];
                    if (json) {
                        opt.valueList[opt.text] = json;
                        if (!json.length) {
                            var json = nodata;
                        }
                    } else {
                        var json = nodata;
                    }
                    render(json);
                })

            }
        };

        this.each(function () {
            var self = this,
                requestTimer = 0,
                focus = false;
            init(self);
            if (opt.isSpeech) {
                self.onwebkitspeechchange = function () {
                    show()
                }
            }

            var filter_time = function (self) {
                var time = setInterval(function () {
                    var now = $.trim(self.value);
                    if (now != '' && now != $(this).data('last-str')) {
                        if (now.length > 0 && now.length < 8) {
                            if (requestTimer == 0) {
                                requestTimer = setTimeout(function () {
                                    show(now)
                                }, 100)
                            }
                        } else {
                            clean()
                        }
                    }
                    $(this).data('last-str', now);
                }, 100);
                $(this).bind('blur', function () {
                    clearInterval(time);
                    setTimeout(function () {
                        clean()
                    }, 200)
                });
            };
            $(self).focus(function () {
                if (!focus) {
                    opt.container[self.id].position($.extend({
                        of: $(self)
                    }, {
                        my: "left top",
                        at: "left bottom",
                        collision: "none"
                    }));
                }
                focus = true;
                filter_time(self);
            }).keyup(function (event) {
                opt.text = self.value;
                var length = opt.text.length,
                    keycode = event.keyCode,
                    index = opt.index;
                if (keycode > 40 || keycode == 8 || keycode == 32) {
                    if (length > 0 && length < 100) {
                        if (requestTimer == 0) {
                            requestTimer = setTimeout(function () {
                                show()
                            }, 100)
                        }
                    } else {
                        clean()
                    }
                } else if (index !== null) {
                    if (keycode == 38) {
                        setIndex(index - 1)
                    } else if (keycode == 40) {
                        setIndex(index + 1)
                    } else if (keycode == 27) {
                        setIndex(0)
                    } else if (keycode == 13) {
                        enter()
                    }
                }
                event.preventDefault()
            }).keydown(function (event) {
                clearTimeout(requestTimer);
                requestTimer = 0
            });
        })
    }
})(jQuery);