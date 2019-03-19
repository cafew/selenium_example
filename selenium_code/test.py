#!/usr/bin/env python
# coding=utf-8
# author:jingjian@datagrand.com
# datetime:2019/3/13 下午4:01
import os, sys, re, json, traceback, time

Flase = False
Ture = True

if __name__ == "__main__":
    # second = time.strftime('%S', time.localtime(time.time()))
    # print(second)
    # if int(second)<40:
    #     print(time.strftime('%Y-%m-%dT%H:%M', time.localtime(time.time())))
    # else:
    #     print(time.strftime('%Y-%m-%dT%H:%M', time.localtime(time.time()+60)))
    # print(time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time())))
    # print(time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time()+60)))
    str="剩余62.7秒"
    pat_num = "\d+"
    result_pat = re.findall(pat_num, str)
    print(result_pat)