#coding=utf-8
from python3.common.core.handler.base_handler import BaseHandler
from python3.modules.sys.service.sys_user_service import SysUserService
from python3.modules.sys.entity.sys_user import SysUser
import time

import json
from uuid import uuid4 as uuid
class LoginControl(BaseHandler):
    def post(self):
        data_json = json.loads(self.request.body)
        result=SysUserService.check_user(data_json)
        if result:
            self.write("true")
            self.set_secure_cookie("unclepw_user_id",result.id)
        else:
            self.write('false')
        #self.write(data_json)


    def get(self):
        unclepw_user_id=str(self.get_secure_cookie("unclepw_user_id"))
        unclepw_user_id=unclepw_user_id[2:len(unclepw_user_id)-1]
        if unclepw_user_id==None:
            self.render("sys/login/login.html")
        else:
            user=SysUserService.find_one(SysUser(id=str(unclepw_user_id)))
            if user!=None:
                self.render("sys/login/login_return_test.html",username=user.login_name)
            else:
                self.render("sys/login/login.html")

class ExitLoginControl(BaseHandler):
    def get(self):
        self.clear_cookie("unclepw_user_id")
        self.redirect("/login")

class TestControl(BaseHandler):
    def get(self):
        time.sleep(10)
        self.write("蹇神🐂🍺")
