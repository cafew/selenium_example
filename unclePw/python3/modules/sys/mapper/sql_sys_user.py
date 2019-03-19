#coding=utf-8
from python3.modules.sys.entity.sys_user import SysUser as form
#select语句涉及的field
field='''
    a.id,a.user_name,a.login_name,a.password    
'''

#from语句
table_name='''
    from ''' +form.table_name +'''   a
'''

#selectAll
def selectAll(entity):
    sql_select_all=\
        "select  "+\
            field+\
        table_name
    return sql_select_all



#delete    id
def delete(entity):
    sql_delete=\
        "delete "+\
        "from  "+form.table_name+"   "\
        "where id="+entity.id
    return sql_delete


#insert    id,user_name,login_name,password
def insertEntity(entity):
    sql_insert=\
        "insert "+form.table_name +" values('"+\
        str(entity.id) + "','" + \
        str(entity.user_name) + "','" + \
        str(entity.login_name) + "','" + \
        str(entity.password) + "'," + \
        str(entity.del_flag) + ",'" + \
        str(entity.remarks) + "','" + \
        str(entity.create_by) + "','" + \
        str(entity.create_date) + "','" + \
        str(entity.update_by) + "','" + \
        str(entity.update_date) + "'" + \
        ")"
    return sql_insert



#update      user_name,login_name,password   id
def updateEntity(entity):
    sql_update=\
        "update user_info set "+\
            "user_name='"+entity.user_name+"',"+ \
            "login_name='"+entity.login_name+"'," + \
            "password='"+entity.password+"'  " +\
        "where id='"+entity.id+"'"
    return sql_update


#selectOne
def selectOneEntity(entity):
    sql_select_one=\
        "select  "+\
            field+\
        table_name+"   "\
        "where a.id='"+entity.id+"'"
    return sql_select_one

#selectOne
def selectOneByLoginName(entity):
    sql_select_by_login_name=\
        "select  "+\
            field+\
        table_name+"   "\
        "where a.login_name='"+entity.login_name+"'"
    return sql_select_by_login_name


