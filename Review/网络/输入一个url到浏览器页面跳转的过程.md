### 一、输入网址

### 二、域名解析  

​      域名解析过程是域名到ip地址的解析过程，浏览器获取url后，首先去浏览器缓冲中查询，查询不到后，依次通过 系统缓冲——>路由器缓冲——>本地DNS服务器——>根域名服务器——>com顶级域名服务器，如果有，就从缓冲中显示页面，  

###三、浏览器与该服务器建立TCP连接(默认端口号80)



### 四、 浏览器向服务器发送请求

### 五、服务器处理请求

服务器可以根据Cookie中的数据，通过遍历内存中的Session集合，从而判断用户的登录状态。如果用户未登录，则展示一些诸如首页的基本宣传数据。如果用户已经登录，通过解析get请求头、post请求体中的参数，查询数据库，返回用户相关数据，填充到视图中。并将此次处理完的内容通过相应的压缩算法，压缩成某个块。

###六、服务器返回http响应

### 七、页面渲染

浏览器收到响应头和响应体后，对页面进行渲染，解析css样式、js交互等



```
1、客户端浏览器通过DNS解析到www.baidu.com 的IP地址220.181.27.48，通过这个IP地址找到客户端到服务器的路径。客户端浏览器发起一个HTTP会话到220.181.27.48，然后通过TCP进行封装数据包，输入到网络层。
2、在客户端的传输层，把HTTP会话请求分成报文段，添加源和目的端口，如服务器使用80端口监听客户端的请求，客户端由系统随机选择一个端口如5000，与服务器进行交换，服务器把相应的请求返回给客户端的5000端口。然后使用IP层的IP地址查找目的端。
3、客户端的网络层不用关心应用层或者传输层的东西，主要做的是通过查找路由表确定如何到达服务器，期间可能经过多个路由器，这些都是由路由器来完成的工作，我不作过多的描述，无非就是通过查找路由表决定通过那个路径到达服务器。
4、客户端的链路层，包通过链路层发送到路由器，通过邻居协议查找给定IP地址的MAC地址，然后发送ARP请求查找目的地址，如果得到回应后就可以使用ARP的请求应答交换的IP数据包现在就可以传输了，然后发送IP数据包到达服务器的地址。
```



```
(1). 浏览器查询 DNS，获取域名对应的IP地址:具体过程包括浏览器搜索自身的DNS缓存、搜索操作系统的DNS缓存、读取本地的Host文件和向本地DNS服务器进行查询等。对于向本地DNS服务器进行查询，如果要查询的域名包含在本地配置区域资源中，则返回解析结果给客户机，完成域名解析(此解析具有权威性)；如果要查询的域名不由本地DNS服务器区域解析，但该服务器已缓存了此网址映射关系，则调用这个IP地址映射，完成域名解析（此解析不具有权威性）。如果本地域名服务器并未缓存该网址映射关系，那么将根据其设置发起递归查询或者迭代查询；

　　(2). 浏览器获得域名对应的IP地址以后，浏览器向服务器请求建立链接，发起三次握手；

　　(3). TCP/IP链接建立起来后，浏览器向服务器发送HTTP请求；

　　(4). 服务器接收到这个请求，并根据路径参数映射到特定的请求处理器进行处理，并将处理结果及相应的视图返回给浏览器；

　　(5). 浏览器解析并渲染视图，若遇到对js文件、css文件及图片等静态资源的引用，则重复上述步骤并向服务器请求这些资源；

　　(6). 浏览器根据其请求到的资源、数据渲染页面，最终向用户呈现一个完整的页面。
```

