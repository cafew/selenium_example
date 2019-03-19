#coding=utf-8


import pymysql

from python3.properties.database_conf import mysql_config_args


def get_conn():
    conn = pymysql.connect(host=mysql_config_args["location"], port=mysql_config_args["port"],
                           user=mysql_config_args["user_name"], passwd=mysql_config_args["password"],
                           db=mysql_config_args["database_name"], charset='utf8')
    return conn

def get_cursor(conn,cursor=pymysql.cursors.DictCursor):
    cursor = conn.cursor(cursor=cursor)
    return cursor