  超文本传输协议HTTP协议被用于在web浏览器和网站服务器之间传递信息，HTTP协议以明文方式发送内容，不提供任何方式进行加密，因此HTTP协议不适合传输敏感信息。

  为了解决HTTP协议的这一缺陷，需要使用另一种协议：安全套接字层超文本传输协议HTTPS，为了数据传输的安全，HTTPS在HTTP的基础上加入了ssl协议，ssl协议是依靠证书来验证服务器的身份，并为浏览器和服务器之间的通信加密

**一、HTTP和HTTPS的基本概念**

　　HTTP：是互联网上应用最为广泛的一种网络协议，是一个客户端和服务器端请求和应答的标准（TCP），用于从WWW服务器传输超文本到本地浏览器的传输协议，它可以使浏览器更加高效，使网络传输减少。

　　HTTPS：是以安全为目标的HTTP通道，简单讲是HTTP的安全版，即HTTP下加入SSL层，HTTPS的安全基础是SSL，因此加密的详细内容就需要SSL。

　　HTTPS协议的主要作用可以分为两种：一种是建立一个信息安全通道，来保证数据传输的安全；另一种就是确认网站的真实性。

**二、HTTP与HTTPS有什么区别？**

　　HTTP协议传输的数据都是未加密的，也就是明文的，因此使用HTTP协议传输隐私信息非常不安全，为了保证这些隐私数据能加密传输，于是网景公司设计了SSL（Secure Sockets Layer）协议用于对HTTP协议传输的数据进行加密，从而就诞生了HTTPS。简单来说，HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，要比http协议安全。

　　HTTPS和HTTP的区别主要如下：

　　1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。

　　2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。

　　3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

　　4、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。



### 三、SSL建立连接过程

1、client向server发送请求，连接到server的443端口，发送的信息主要是随机数一和支持的加密方式和ssl版本

2、server收到信息给与响应，内容包括随机数2和协商过后的加密算法

3、server发送的第二个响应报文是数字证书，这数字证书（经过hash计算得到数字摘要，再用ca的私钥加密得到数字签名）其实就加密这ca的公钥，

4、client要验证证书是否有效，验证通过之后就得到了证书的公钥

5、client生成随机数3，然后用证书的公钥加密后发给server

6、server用自己的私钥解密得到随机数三

7、client和server用确定的加密方法将前三个随机数生成一个`对话密钥` 用来接下来的通信

8、客户端通过会话秘钥加密一条消息发送给服务端，主要验证服务端是否正常接受客户端加密的消息。

9、同样服务端也会通过会话秘钥加密一条消息回传给客户端，如果客户端能够正常接受的话表明SSL层连接建立完成了。