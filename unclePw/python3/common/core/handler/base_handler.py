#coding=utf-8
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("uncle_pw_user_id")

    def check_login(self):
        unclepw_user_id = self.get_secure_cookie("unclepw_user_id")
        if unclepw_user_id == None:
            self.render("sys/login/login.html")
        else:
            self.redirect("https://www.baidu.com")