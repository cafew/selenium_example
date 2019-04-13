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
        js_login = "login()"
        browser.execute_script(js_login)
        # 首先我们要根据弹窗结果读取状态，如果是我们想要的状态则继续下一步操作，否则报错
        login_message_show_return_param = dict()
        if not utils.while_else_sleep(page_check.login_message_show, {"browser": browser},
                                      login_message_show_return_param):
            raise Exception(login_message_show_return_param["message"])
        time.sleep(3)
        # 三秒之后会刷新页面，要确保页面是否已经刷新成功，否则报错
        login_success_return_param = dict()
        if not utils.while_else_sleep(page_check.login_success, {"browser": browser}, login_success_return_param):
            raise Exception(login_message_show_return_param["message"])
        # 找到对应的 定时抢课页面 的a标签
        select_class_a = browser.find_elements_by_tag_name("li")[0].find_element_by_tag_name("a")
        select_class_a.click()
        # 判定子页面是否刷新成功
        select_class_page_show_return_param = dict()
        if not utils.while_else_sleep(page_check.select_class_page_show, {"browser": browser},
                                      select_class_page_show_return_param):
            raise Exception(select_class_page_show_return_param["message"])
        # 切换iframe
        browser.switch_to.frame(browser.find_element_by_id("child_frame"))
        # 设置好开抢时间 如果秒数小于40 那就当前时间，如果秒数大于40，则推迟一分钟
        second = int(time.strftime('%S', time.localtime(time.time())))
        time_str = time.strftime('%Y-%m-%dT%H:%M', time.localtime(time.time() + 60))
        if second >= 40:
            time_str = time.strftime('%Y-%m-%dT%H:%M', time.localtime(time.time() + 120))
        # 填入日期
        utils.write_into_date_by_id(browser, "date", time_str)
        # 点击 生成抢课列表
        js_create_class_list = "create_class_list()"
        browser.execute_script(js_create_class_list)
        # 判定一下是否出现弹窗表示时间选择有误
        time_error_div_show_return_param = dict()
        if utils.while_else_sleep(page_check.time_error_div_show, {"browser": browser},
                                  time_error_div_show_return_param, times_max=4):
            raise Exception(time_error_div_show_return_param["message"])
        # 判定table是否已经展示出来
        class_table_show_return_param = dict()
        if not utils.while_else_sleep(page_check.class_table_show, {"browser": browser}, class_table_show_return_param):
            raise Exception(class_table_show_return_param["message"])
        # 选择我们需要的课程 例如 计算机课
        trs = browser.find_element_by_id("class_list").find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        find_flag = False
        for each_tr in trs:
            tds = each_tr.find_elements_by_tag_name("td")
            if tds[1].text == "计算机课":
                # time.sleep(1)
                left_time_str = tds[3].text
                pat_num = "\d+"
                result_pat = re.findall(pat_num, left_time_str)
                if len(result_pat) > 0:
                    left_time = int(result_pat[0])
                    click_button_param = {"browser": browser, "button": tds[2].find_element_by_tag_name("button")}
                    click_button_return_param = dict()
                    if not utils.while_else_sleep(page_check.click_button, click_button_param,
                                                  click_button_return_param, times_max=(left_time+3)*10,
                                                  sleep_time=0.1):
                        raise Exception(click_button_return_param["message"])
                    # 判定抢课是否成功（有无弹窗，弹窗内容）
                    select_fail_message_show_return_param = dict()
                    if not utils.while_else_sleep(page_check.select_fail_div_show, {"browser": browser},
                                                  select_fail_message_show_return_param, times_max=4):
                        raise Exception(browser.find_element_by_id("class_list").find_element_by_tag_name("tbody").
                                        find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("td")[3].text)
                else:
                    raise Exception(tds[3].text)
                find_flag = True
                break


    except Exception as e:
        print(e.args[0])

