#!/usr/bin/env python
# coding=utf-8
# author:jingjian@datagrand.com
# datetime:2019/3/18 下午12:00
import os, sys, re, json, traceback
# from selenium import webdriver
from selenium.webdriver.remote import webdriver

Flase = False
Ture = True


# class my_chrome_webdriver(webdriver):
#     def __init__(self, local_server, session_id):





if __name__ == "__main__":
    # driver=webdriver.Chrome()
    # executor_url = driver.command_executor._url
    # session_id = driver.session_id
    # print(session_id)
    # print(executor_url)
    # driver.get("https://www.baidu.com/")


    executor_url = "http://localhost:61403"
    session_id = "0181f6e3e7f4868b9cbf9301ee942275"
    # webdriver.RemoteConnection
   