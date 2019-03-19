#coding=utf-8
from python3.common.core.handler.base_handler import BaseHandler
from python3.modules.sys.service.sys_user_service import SysUserService
import json



class RegisterControl(BaseHandler):
    def post(self):
        data_json = json.loads(self.request.body)
        result=SysUserService.add_user(data_json=data_json)
        if result:
            self.write("True")
        else:
            self.write(data_json)


    def get(self):

        self.render("sys/login/register.html")


class RegisterCheck(BaseHandler):
    def post(self):
        data_json = json.loads(self.request.body)
        #  1检查登陆名是否重复
        method_num=data_json["method_num"]
        if method_num=="1":
            self.write(SysUserService.check_login_name(data_json["user_name"]))
        else:
            self.write("method index wrong")

