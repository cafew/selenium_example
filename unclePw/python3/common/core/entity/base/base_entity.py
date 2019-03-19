#coding=utf-8
from python3.common.util.conn_database import get_cursor,get_conn
from python3.common.util import util
import sys
from datetime import datetime
class BaseEntity(object):
    table_name=""
    table_structure=[]
    def __init__(self,id=None,remarks=None,del_flag=0):
        self.id=id
        self.remarks=remarks
        self.del_flag=del_flag
        self.create_by=None
        self.create_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_by=None
        self.update_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def print_self(self):
        print(self.__dict__)

    @classmethod
    def get_object(cls):
        return cls()

    @classmethod
    def get_sql_module(cls):
        modules=str(cls.__module__).split(".")
        sql_module=""
        for module in modules[:len(modules)-2]:
            sql_module+=module+"."
        sql_module+="mapper."
        sql_module+="sql_"+cls.table_name
        return __import__(sql_module, fromlist=True)

    #得到表结构
    @classmethod
    def get_table_structure(cls):
        conn=get_conn()
        if len(cls.table_structure)==0:
            table_structure = []
            cursor = get_cursor(conn,None)
            cursor.execute("desc  "+cls.table_name)
            data=cursor.fetchall()
            for each in data:
                table_structure.append(each[0])
            cls.table_structure=table_structure
            cursor.close()
        conn.close()
        return cls.table_structure

    @classmethod
    def find_all(cls,self):
        conn = get_conn()
        #暂时所有的类的sql都直接放置在sql文件夹下不重新进行区分
        module = cls.get_sql_module()
        cursor=get_cursor(conn)
        cursor.execute(module.selectAll(self))
        data=cursor.fetchall()
        base_entity_list=[]
        for base_entity_map in data:
            base_entity=cls.get_object()
            for key in base_entity_map:
                setattr(base_entity,key,base_entity_map[key])
            base_entity_list.append(base_entity)
        cursor.close()
        conn.close()
        return base_entity_list

    @classmethod
    def delete(cls,self):
        conn = get_conn()
        cursor = get_cursor(conn)
        module = cls.get_sql_module()
        result="删除成功"
        try:
            num=cursor.execute(module.sql_delete)
            conn.commit()
            if num==0:
                result="没有找到id="+id+"的数据"
        except:
            result="删除出错"

        cursor.close()
        conn.close()
        return result

    @classmethod
    def insert(cls, base_entity):
        conn = get_conn()
        cursor = get_cursor(conn)
        module = cls.get_sql_module()
        #先得到表结构
        table_structure=cls.get_table_structure()
        value=[]
        for field in table_structure:
            value.append(getattr(base_entity,field,""))
        #print value
        #再生成增加语句
        result="新增成功"
       # try:
        if True:
            num=cursor.execute(module.insertEntity(base_entity))
            conn.commit()
            if num==0:
                result="新增失败"
        # except:
        #     result="出现错误"
        cursor.close()
        conn.close()
        return result

    @classmethod
    def update(cls,base_entity):
        conn = get_conn()
        cursor=get_cursor(conn)
        module = cls.get_sql_module()
        table_structure = cls.get_table_structure()
        value = []
        for field in table_structure:
            value.append(getattr(base_entity, field, ""))
        id=value[0]
        value=value[1:]
        value.append(id)
        #再生成修改语句
        result="修改成功"
        try:
            num=cursor.execute(module.sql_update,value)
            #print cursor._executed
            conn.commit()
            if num==0:
                result="修改失败(没有该id,或者并没有变化)"
        except:
            result="出现错误"
        cursor.close()
        conn.close()
        return result

    @classmethod
    def save(cls, base_entity):
        if base_entity.id==None or base_entity.id== "":
            base_entity.id=str(util.getUuid())
            base_entity.create_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(base_entity.id)
            return cls.insert(base_entity)
        else:
            base_entity.update_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return cls.update(base_entity)


    @classmethod
    def find_one(cls,entity):
        conn = get_conn()
        # 暂时所有的类的sql都直接放置在sql文件夹下不重新进行区分
        module = cls.get_sql_module()
        cursor = get_cursor(conn)
        cursor.execute(module.selectOneEntity(entity))
        data = cursor.fetchone()
        base_entity=None
        if data!=None:
            base_entity = cls.get_object()
            for key in data:
                setattr(base_entity, key, data[key])

        cursor.close()
        conn.close()
        return base_entity

if __name__=="__main__":
    print(BaseEntity.get_sql_module())



