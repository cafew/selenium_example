#!/usr/bin/env python
# coding=utf-8
# author:jingjian@datagrand.com
# datetime:2019/3/11 上午11:00
import os, sys, re, json, traceback
from python3.common.core.handler.base_handler import BaseHandler

Flase = False
Ture = True


class SelectClass(BaseHandler):
    def post(self):
        pass
    def get(self):
        self.render("selenium/select_class.html")

class TableInput(BaseHandler):
    def post(self):
        pass
    def get(self):
        self.render("selenium/table_input.html")

if __name__ == "__main__":
    pass
