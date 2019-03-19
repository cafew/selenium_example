#coding=utf-8
from python3.common.util.conn_database import get_cursor,get_conn
from python3.common.core.entity.base.base_entity import BaseEntity
from datetime import datetime

class SysUser(BaseEntity):
    table_name="sys_user"
    def __init__(self,id=None,user_name=None,login_name=None,password=None,remarks=None,del_flag=0):
        BaseEntity.__init__(self,id,remarks,del_flag)
        self.user_name=user_name
        self.login_name=login_name
        self.password=password

    @classmethod
    def find_by_login_name(cls, entity):
        conn = get_conn()
        # 暂时所有的类的sql都直接放置在sql文件夹下不重新进行区分
        moudle = cls.get_sql_module()
        cursor = get_cursor(conn)
        cursor.execute(moudle.selectOneByLoginName(entity))
        data = cursor.fetchone()
        base_entity = None
        if data != None:
            base_entity = cls.get_object()
            for key in data:
                setattr(base_entity, key, data[key])

        cursor.close()
        conn.close()
        return base_entity

if __name__=="__main__":
    #user1=SysUser()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user1=SysUser(user_name="test",login_name="test",password="test",remarks="")

    print(SysUser.save(user1))