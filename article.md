介绍
=========================================
一篇关于selenium初步尝试的文章
****
	
|Author|景健|
|---|---|
|E-mail|jingjian@datagrand.com|




## 背景
北京时间晚上十一点，突然电脑右下角的QQ弹出了一条消息，"在？"    

都9012年了还会有人单独发个"在"然后人就失踪了？有事情找就直接说事情嘛，你不说事情，我怎么知道我应该"在"还是应该"不在"呢？  

鼠标移动到右下角准备点击"取消闪烁"时发现，是小美。

感觉空气中突然弥漫着一种说不明的东西，还是忍不住回复了一句，"在，什么事情？"

"你明天下午一点方便使用电脑吗？"  

唉，有什么事情为什么不可以一口气说完呢，为什么总要说半句呢，如果我在这个人面前我肯定一个大嘴巴子上去了。但，这是小美。"方便"。

"我明天选修课要抢课，你方便的话帮我一下呗，我和朋友约了出去玩了。"

果不其然，在我学会了如何修电脑、如何恢复数据、如何下载视频等技能后，又有新的技能树即将需要被点亮。不过区区抢选修课能难到我？我不仅要抢到，还要抢得漂亮，抢得安逸，抢得让自己都佩服！

"No problem！抢课地址，账号，密码，课程名。"

这干脆利落的语气，完美。

## 需求分析
抢课只是一件小事，无非是打开浏览器，等时间到了疯狂点击。但想必大多数人都在大学时候有过惨痛的经历，无外乎学校网络太差，热门课程抢的人数太多自己不一定能抢到。同样，我也并不能保证自己在第二天下午一点的时候盯着屏幕不停地点，或者舒服一点用鼠标连点器不停地点，就能很大可能地抢到需要的课程。

学校的网络没法拯救，只能拯救自身的网络；抢同一门课程的人数多，我们就需要开更多的窗口去抢！

很好，看来我们需要搞定一段自动抢课的代码，然后在自己机器上部署、在舍友机器上部署、在云环境部署、在网络好的其他机器部署，想必这总能最大可能性抢到想要的课程了吧。

我仿佛看到了一个幕后黑手看着自己的屏幕嘿嘿嘿地笑着:
    
    王小明 世界电子竞技    抢课中...
    吴小杰 日本av赏析     抢课成功
    陈小龙 基础烹饪知识    抢课成功
    刘小乡 莎士比亚戏剧选  抢课中...
    ...

![1][1]  
抢课，我从来没怕过谁。

## 方案设计
`本文只着重介绍selenium相关使用，不会对整个方案进行完整的实现`

此前在学习python爬虫的时候接触过selenium的知识，完全可以适配这样浏览器操作场景。

可以先用selenium写一个操作浏览器抢课的脚本，再用flask来接收外部的请求命令执行对应的抢课脚本，用docker打包成镜像，再到能暂时操作的所有电脑，云服务器部署一套。

等快到抢课时间了，安安心心躺在椅子上，执行一下批量发送请求的脚本，就可以静待抢课成功的好消息了。

我只想发出三个字的声音：还！有！谁！

## selenium简单介绍
官网介绍
    
    Selenium is a suite of tools to automate web browsers across many platforms.
    runs in many browsers and operating systems
    can be controlled by many programming languages and testing frameworks.
    Selenium 官网：http://seleniumhq.org/
    Selenium Github 主页：https://github.com/SeleniumHQ/selenium
    
百度百科
    
    Selenium是一个用于Web应用程序测试的工具。
    Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。
    支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。
    这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。
    测试系统功能——创建回归测试检验软件功能和用户需求。
    支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。
    
功能
    
    框架底层使用JavaScript模拟真实用户对浏览器进行操作。
    测试脚本执行时，浏览器自动按照脚本代码做出点击，输入，打开，验证等操作，就像真实用户所做的一样，从终端用户的角度测试应用程序。
    使浏览器兼容性测试自动化成为可能，尽管在不同的浏览器上依然有细微的差别。
    使用简单，可使用Java，Python等多种语言编写用例脚本。
    
简单来说，起初selenium是一套用于web自动化测试的工具，其本身具备了对多种浏览器/操作系统的兼容支持，且能通过多种语言进行操作控制。
但其强大的功能不仅仅适用于web自动化测试领域，同样也被广泛地使用在爬虫以及rpa(Robotic Process Automation)相关的业务场景上。
而我们现在需要实现的可以说就是一个简单的rpa功能。

## 开发及测试环境介绍
笔者开发环境:Mac OS、PyCharm、python3.6、chrome

笔者提供的测试网址:www.uncleyiba.com
    
    该网址可自行注册，或者使用测试账号nvshen/nvshen
    因为是沿用的很久之前刚接触tornado时候的代码，所以对tornado的使用有一些误解。
    因此可能导致如果多人使用线上测试环境，会有一些问题出现。
    所以建议可以本地启一套测试环境。
    
测试网站及selenium脚本源码:[selenium_example](https://github.com/uncleYiba/selenium_example)（https://github.com/uncleYiba/selenium_example）
    
    使用方式见readme.md
    
## selenium使用了解
### 关注点
对于selenium而言，需要实现我们的需求，着重要关注两点：

    1.页面元素定位  
    是否能准确获取到我们需要进行操作的元素  
    
    2.页面元素操作  
    点击、填入、清楚内容、获取数据、双击、按住、松开、拖动等  

### 开发者工具使用
既然是操作浏览器进行需求实现，那我们必然要对前端有一些了解。
也就是说html和js相关知识需要有一些涉猎，另外需要会操作chrome的开发者工具，即Mac的option+command+i,或者是windows的F12。

![2][2]

首先点击红色按钮，再选取需要定位的具体元素信息，即可获取到该元素在html页面中的所有信息。

![3][3]

以登陆按钮为例，我们发现其并没有设置id属性，但是其onclick触发的方法直接表现了出来，我们便可以通过两种方式触发对应的登陆事件。
可以根据class_name,tag_name等来获取元素并执行点击事件，或者可以直接执行login()的js从而触发登陆事件。

    <button class="button" onclick="login()" style="margin-left:18%">登陆</button>

### selenium元素定位
selenium提供了一系列的方法通过元素的属性定位页面中的具体元素，其属性包括并不仅限于id、name、class_name、tag_name、xpath、css_elector等，通过WebDriver对象我们可以调用对应的find_element_by方法。
例如以下html代码：
    
    <input id="login" type="button">登陆</input>

我们获取其元素的方法就是find_element_by_id，其他具体的可用方法列表如下:

![4][4]

如果方法名中只是"element"则获取到的是单个元素对象，而如果是"elements"的话则获取到的是该种类对象的一个list集合。

对于单个元素对象而言，其所有可执行方法或属性如下:

![5][5]

从列表中我们可以清晰地看见单个元素对象也具有find_element_by的一系列方法，意味着我们可以定位一个父元素，再通过父元素定位其子元素，一层一层定位准确。

### selenium元素操作
`其中browser为浏览器对象`

常见的html元素包括:输入框input,按钮button,复选框checkbox,单选框radio,下拉选择框select,时间选择框date,富文本框textarea以及一些用于显示文本的标签包括不仅限于div、span、p等。

输入框input:
    
    <input type="text" id="last_name" name="last_name">
    
需要实现对其输入的功能，可使用如下代码:

    browser.find_element_by_name("last_name").send_keys("测试文本")
    
按钮button:

    <button id="submit" onclick="alertDiv('提交成功！')">提交</button>
    
需要实现对其进行点击的功能，可使用如下代码:

    browser.find_element_by_id("submit")[1].click()
    
复选框checkbox:

    <input type="checkbox" name="q1" value="0">一&nbsp;&nbsp;
    <input type="checkbox" name="q2" value="1">二&nbsp;&nbsp;
    <input type="checkbox" name="q3" value="2">三&nbsp;&nbsp;
    <input type="checkbox" name="q4" value="3">四

需要实现对其value=0和value=1复选框的选中功能，可使用如下代码:

    browser.find_element_by_name("q1").click()
    browser.find_element_by_name("q2").click()
    
单选框radio:

    <input type="radio" name="team" value="0">是&nbsp;&nbsp;
    <input type="radio" name="team" value="1">否
    
需要实现对其value=0，显示为"是"的单选框的选择功能，可使用如下代码:
    
    browser.find_elements_by_name("team")[0].click()
    
下拉选择框select:
    
    <select name="gender">
        <option value="0">男</option>
        <option value="1">女</option>
        <option value="2">其他</option>
    </select>
    
需要实现对其下拉选项"男"的选择功能，可使用如下代码:
    
    browser.find_element_by_name("gender").find_elements_by_tag_name("option")[0].click()
    
时间选择框date:
    
    <input type="date" name="birthday">
    
需要实现对其时间的输入，可使用如下代码:
    
    js_input = '''$("input[name={0}]").val("{1}")'''.format("birthday", "2000-01-01")
    browser.execute_script(js_input)
    
PS:鉴于各种日期控件比较多，个人使用看来直接使用js对其赋值是一种比较方便的方式

富文本框textarea:
    
    <textarea name="textarea"></textarea>
    
需要实现对其输入的功能，可使用如下代码:
    
    browser.find_element_by_name("textarea").send_keys("测试文本")

至于其他一些用于显示文本的标签，例如:

    <span id="name">嬴政</span>
    
需要实现对其文本内容的获取，可使用如下代码:
    
    text = browser.find_element_by_id("name").text
    
至于元素的点住，松开，拖动等操作将结合在实际案例的代码中











----------------
[1]:imgs/1.png
[2]:imgs/2.png
[3]:imgs/3.png
[4]:imgs/4.png
[5]:imgs/5.png


