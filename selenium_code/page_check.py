#!/usr/bin/env python
# coding=utf-8
# author:jingjian@datagrand.com
# datetime:2019/3/13 下午2:49
import os, sys, re, json, traceback
from selenium.common.exceptions import NoSuchElementException
from selenium_code import utils

def login_message_show(param, return_param):
    browser = param["browser"]
    try:
        alert_div=browser.find_element_by_class_name("alert")
        message_div=alert_div.find_element_by_tag_name("div")
        if "正确" in message_div.text:
            return True
        else:
            return_param["message"] = message_div.text
            if "用户名或密码错误" in message_div.text:
                return_param["status"] = "over"
            return False
    except NoSuchElementException:
        # print(traceback.format_exc())
        return_param["message"] = "元素不存在"
        return False


def login_success(param, return_param):
    browser = param["browser"]
    try:
        user_name_div = browser.find_element_by_tag_name("div")
        logout_a = user_name_div.find_element_by_tag_name("a")
        if "退出登录" == logout_a.text:
            return True
        else:
            return_param["message"] = "页面尚在加载中"
            return False
    except NoSuchElementException:
        # print(traceback.format_exc())
        return_param["message"] = "页面尚在加载中"
        return False


def select_class_page_show(param, return_param):
    # 切换iframe
    browser = param["browser"]
    browser.switch_to.frame(browser.find_element_by_id("child_frame"))
    try:
        h1 = browser.find_element_by_tag_name("h1")
        if "测试用抢课页面" == h1.text:
            browser.switch_to.parent_frame()
            return True
        else:
            browser.switch_to.parent_frame()
            return_param["message"] = "页面尚在加载中"
            return False
    except NoSuchElementException:
        # print(traceback.format_exc())
        browser.switch_to.parent_frame()
        return_param["message"] = "页面尚在加载中"
        return False


def table_input_page_show(param, return_param):
    # 切换iframe
    browser = param["browser"]
    browser.switch_to.frame(browser.find_element_by_id("child_frame"))
    try:
        h1 = browser.find_element_by_tag_name("h1")
        if "测试用表单提交页面" == h1.text:
            browser.switch_to.parent_frame()
            return True
        else:
            browser.switch_to.parent_frame()
            return_param["message"] = "页面尚在加载中"
            return False
    except NoSuchElementException:
        # print(traceback.format_exc())
        browser.switch_to.parent_frame()
        return_param["message"] = "页面尚在加载中"
        return False


def class_table_show(param, return_param):
    browser = param["browser"]
    try:
        table = browser.find_element_by_tag_name("table")
        if table.is_displayed():
            return True
        else:
            return_param["message"] = "表格尚在加载中"
            return False
    except NoSuchElementException:
        # print(traceback.format_exc())
        browser.switch_to.parent_frame()
        return_param["message"] = "表格尚在加载中"
        return False


def select_success_show(param, return_param):
    browser = param["browser"]
    try:
        select_success_div = browser.find_element_by_class_name("alert")
        return_param["message"] = select_success_div.find_element_by_tag_name("div").text
        return True
    except NoSuchElementException:
        return False



def click_button(param, return_param):
    browser = param["browser"]
    button = param["button"]
    try:
        button.click()
        select_success_div = browser.find_element_by_class_name("alert")
        return_param["message"] = select_success_div.find_element_by_tag_name("div").text
        return True
    except NoSuchElementException:
        return_param["message"] = "抢课尚未开始"
        return False
    except:
        return False


def time_error_div_show(param, return_param):
    browser = param["browser"]
    try:
        time_error_div = browser.find_element_by_class_name("alert")
        return_param["message"] = time_error_div.find_element_by_tag_name("div").text
        return True
    except NoSuchElementException:
        return False



def select_fail_div_show(param, return_param):
    browser = param["browser"]
    try:
        time_error_div = browser.find_element_by_class_name("alert")
        return_param["message"] = time_error_div.find_element_by_tag_name("div").text
        return True
    except NoSuchElementException:
        return False






if __name__ == "__main__":
    pass
