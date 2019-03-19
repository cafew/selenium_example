#coding = utf-8
from python3.modules.sys.entity.sys_user import SysUser
class SysUserService(SysUser):
    def check_login_name(login_name):
        entity=SysUser(login_name=login_name)
        #entity.login_name=login_name
        user = SysUser.find_by_login_name(entity)
        if user == None:
            return "True"
        else:
            return "False"

    def add_user(data_json):
        try:
            login_name = data_json["login_name"]
            user_name = data_json["user_name"]
            pwd = data_json["pwd"]
            user = SysUser(login_name=login_name, user_name=user_name, password=pwd)
            if (SysUserService.check_login_name(login_name) == "False"):
                return False

            SysUser.save(user)
        except:
            return False
        return True

    def check_user(data_json):
        username = data_json["username"]
        password = data_json["password"]
        entity = SysUser(login_name=username)
        user = SysUser.find_by_login_name(entity)
        if user != None and user.password == password:
            return user
        else:
            return False