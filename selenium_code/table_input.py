#!/usr/bin/env python
# coding=utf-8
# author:jingjian@datagrand.com
# datetime:2019/3/14 上午11:01
import os, sys, re, json, traceback, time
from selenium import webdriver
from selenium_code import utils, page_check
from selenium.webdriver import ActionChains

Flase = False
Ture = True

if __name__ == "__main__":
    try:
        # 加启动配置
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        # 全屏效果
        # option.add_argument('--kiosk')
        # 打开chrome浏览器
        browser = webdriver.Chrome(chrome_options=option)
        # 设置窗口大小
        browser.set_window_size(1500, 1000)

        # ======以下是rpa流程======
        browser.get("http://www.uncleyiba.com")
        # 填入用户名和密码
        utils.write_into_input_by_id(browser, "username", "nvshen")
        utils.write_into_input_by_id(browser, "password", "nvshen")
        # 执行登陆js
        js_login="login()"
        browser.execute_script(js_login)
        # 首先我们要根据弹窗结果读取状态，如果是我们想要的状态则继续下一步操作，否则报错
        login_message_show_return_param = dict()
        if not utils.while_else_sleep(page_check.login_message_show, {"browser": browser}, login_message_show_return_param):
            raise Exception(login_message_show_return_param["message"])
        time.sleep(3)
        # 三秒之后会刷新页面，要确保页面是否已经刷新成功，否则报错
        login_success_return_param = dict()
        if not utils.while_else_sleep(page_check.login_success, {"browser": browser}, login_success_return_param):
            raise Exception(login_message_show_return_param["message"])
        # 找到对应的 定时抢课页面 的a标签
        select_class_a = browser.find_elements_by_tag_name("li")[1].find_element_by_tag_name("a")
        select_class_a.click()
        # 判定子页面是否刷新成功
        table_input_page_show_return_param = dict()
        if not utils.while_else_sleep(page_check.table_input_page_show, {"browser": browser},
                                      table_input_page_show_return_param):
            raise Exception(table_input_page_show_return_param["message"])
        # 切回iframe
        browser.switch_to.frame(browser.find_element_by_id("child_frame"))
        # 进行表单填报
        # 姓
        utils.write_into_input_by_name(browser, "last_name", "张")
        # 名
        utils.write_into_input_by_name(browser, "first_name", "三")
        # 性别
        utils.select_by_name(browser, "gender", "男")
        # 出生日期
        utils.write_into_date_by_name(browser, "birthday", "2000-01-01")
        # 班级
        utils.select_by_name(browser, "class", "三年二班")
        # 学号
        utils.write_into_input_by_name(browser, "number", "12345678")
        # 是否是少先队员
        utils.select_radio_by_name(browser, "team", "是", {"0": "是", "1": "否"})
        # 是否是三好学生
        utils.select_radio_by_name(browser, "student", "是", {"0": "是", "1": "否"})
        # 是否喝旺仔牛奶
        utils.select_radio_by_name(browser, "milk", "是", {"0": "是", "1": "否"})
        # 问题1
        utils.select_checkbox_by_name(browser, "q1", "陈运文", {"0": "马云", "1": "陈运文", "2": "马化腾", "3": "李彦宏"})
        # 问题2
        utils.select_checkbox_by_name(browser, "q2", "纪达麒", {"0": "张建锋", "1": "纪达麒", "2": "熊明华", "3": "李一男"})
        # 问题3
        utils.select_checkbox_by_name(browser, "q3", "冯佳妮", {"0": "李旭辉", "1": "冯佳妮", "2": "任宇昕", "3": "陆奇"})
        # 问题4
        utils.select_checkbox_by_name(browser, "q4", "文本智能处理", {"0": "图像智能处理", "1": "文本智能处理", "2": "语音智能处理", "3": "以上都是"})
        # 问题5
        utils.select_some_checkbox_by_name(browser, "q5", ["愿意", "愿意", "愿意", "以上都是"],
                                           {"0": "愿意", "1": "愿意", "2": "愿意", "3": "以上都是"})
        # 文件
        utils.upload_file_by_name(browser, "file", os.path.abspath("test.txt"))
        # 富文本
        utils.write_into_input_by_name(browser, "textarea", "我超想加入达观数据哒！！！")
        # 拖动验证
        # 1.分别得到两个div的left和top
        div1 = browser.find_element_by_id("div1")
        div2 = browser.find_element_by_id("div2")
        left_div1 = div1.location.get("x")
        top_div1 = div1.location.get("y")
        left_div2 = div2.location.get("x")
        top_div2 = div2.location.get("y")
        # 2.设置好ActionChains对象用于进行键鼠操作
        actions = ActionChains(browser)
        actions.click_and_hold(div1) # a.按住div1
        actions.move_by_offset(left_div2 - left_div1, top_div2 - top_div1) # b.横纵坐标移动（相对坐标）
        actions.release() # c.释放鼠标
        actions.perform() # d.执行动作流

        # 提交
    except Exception as e:
        print(traceback.format_exc())
        print(e.args[0])

