# ajax
- asynchronous javascript and xml
- 异步JS及XML
- 与服务器交换数据，部分更新网页，不重新加载整个页面
- 不是新的编程语言，基于JS的新方法,2005年google推广
- 可以创建更好、更快以及更友好的WEB应用程序
- ajax基于js和HTTP请求(http requests)
- jQuery底层对ajax进行了封装，使得我们在进行ajax操作时，不必向原生js中那么复杂
- ajax方法
    - 返回XMLHttpRequest对象
    - $.get()
        - $.get(url,{请求参数},function(data){},'json')
    - $.post()
        - $.post(url,{请求参数},function(data){},'json')
    - $.ajax()
        - $.ajax({})

# 使用ajax
- 具有web服务器，通过浏览器执行http请求
- 直接打开html文件使用的是file协议，使用http协议需要搭建web服务，然后使用浏览器访问
