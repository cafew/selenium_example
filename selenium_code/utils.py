#!/usr/bin/env python
# coding=utf-8
# author:jingjian@datagrand.com
# datetime:2019/3/13 上午10:45
import os, sys, re, json, traceback, time

Flase = False
Ture = True


def nothing_happened_func(param,return_param):
    '''
    默认执行的空方法
    :param param:包含webDriver对象等信息
    :param return_param:返回的结果
    '''
    pass


def while_else_sleep(func, param, return_param, false_func=nothing_happened_func, times_begin=0, times_max=20, sleep_time=1):
    '''
    :param func:重复执行的方法
    :param param:func方法携带的参数
    :param return_param:func方法返回的参数
    :param false_func:如果func返回结果为false，需要执行的函数
    :param times_begin:开始的次数
    :param times_max:最大重复执行次数
    :param sleep_time:每次等待时间
    :return:boolean
    '''
    times = times_begin
    while True:
        #print("{0}:{1}[max:{2}]".format(func, times, times_max))
        times += 1
        if func(param, return_param):
            break
        else:
            time.sleep(sleep_time)
            false_func(param, return_param)
        if times >= times_max:
            return False
        if return_param.get("status", "") == "over":
            return False
    return True


def write_into_input_by_name(browser, name, content):
    ele = browser.find_element_by_name(name)
    ele.send_keys(content)


def write_into_input_by_id(browser, ele_id, content):
    ele = browser.find_element_by_id(ele_id)
    ele.send_keys(content)

def write_into_date_by_id(browser, ele_id, date):
    js_input = '''$("#{0}").val("{1}")'''.format(ele_id, date)
    browser.execute_script(js_input)

def write_into_date_by_name(browser, ele_name, date):
    js_input = '''$("input[name={0}]").val("{1}")'''.format(ele_name, date)
    browser.execute_script(js_input)

def select_by_name(browser, ele_name, content):
    ele = browser.find_element_by_name(ele_name)
    options = ele.find_elements_by_tag_name("option")
    for each_option in options:
        if each_option.text==content:
            each_option.click()
            break

def select_radio_by_name(browser, ele_name, content, value_dict):
    eles = browser.find_elements_by_name(ele_name)
    for each_ele in eles:
        value = each_ele.get_attribute("value")
        if value_dict.get(value,"")==content:
            each_ele.click()
            break


def select_checkbox_by_name(browser, ele_name, content, value_dict):
    eles = browser.find_elements_by_name(ele_name)
    for each_ele in eles:
        value = each_ele.get_attribute("value")
        if value_dict.get(value, "") == content:
            each_ele.click()
            break

def select_some_checkbox_by_name(browser, ele_name, contents, value_dict):
    eles = browser.find_elements_by_name(ele_name)
    for each_ele in eles:
        value = each_ele.get_attribute("value")
        if value_dict.get(value, "") in contents:
            each_ele.click()


def upload_file_by_name(browser, ele_name, file_path):
    ele = browser.find_element_by_name(ele_name)
    ele.send_keys(file_path)




if __name__ == "__main__":
    pass
