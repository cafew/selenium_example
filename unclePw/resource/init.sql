create database  uncle_pw  default character set utf8 collate utf8_general_ci;

use uncle_pw;

create table sys_user(
   id varchar(32) NOT NULL PRIMARY KEY,
   user_name VARCHAR(36),
   login_name VARCHAR(36),
   password varchar(36),
   del_flag int(1),
   remarks varchar(36),
   create_by varchar(36),
   create_date datetime,
   update_by varchar(36),
   update_date datetime
);