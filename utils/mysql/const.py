#!/usr/bin/env python  
# _#_ coding:utf-8 _*_ 
SQL_PERMISSIONS = {
   "CREATE_USER":{
       "desc":"DDL-创建用户"
   },
   "CREATE_DATABASE":{
       "desc":"DDL-创建数据库"
   },
   "CREATE_TABLE":{
       "desc":"DDL-创建表权限"
    },
   "CREATE_VIEW":{
       "desc":"DDL-创建视图"
   },
   "CREATE_INDEX":{
       "desc":"DDL-创建索引"
   },
   "CREATE_EVENT":{
       "desc":"DDL-创建事件"
   },
   "CREATE_TRIGGER":{
       "desc":"DDL-创建触发器"
   },
   "CREATE_PROCEDURE":{
       "desc":"DDL-创建存储过程"
   },
   "CREATE_FUNCTION":{
       "desc":"DDL-创建自定义函数"
   },
   "DROP_TABLE":{
       "desc":"DDL-删除表"
   },
   "ALTER_TABLE":{
       "desc":"DDL-修改表"
   }, 
   "DESTRIBE":{
       "desc":"DDL-查看表结构"
   },   
   "SHOW_CREATE":{
       "desc":"DDL-查看表结构"
   },   
   "RENAME_TABLE":{
       "desc":"DDL-重命名表"
   },  
   "TRUNCATE_TABLE":{
       "desc":"DDL-清空表"
   },     
   
      
   "INSERT_INTO":{
       "desc":"DML-写入数据"
   },    
   "UPDATE":{
       "desc":"DML-更新数据"
   },
   "DELETE_FROM":{
       "desc":"DML-删除数据"
   },
   "SELECT":{
       "desc":"DQL-查询数据"
   },
   "EXPLAIN":{
       "desc":"DQL-数据分析"
   },
   
   
   "SHOW_TABLES":{
       "desc":"SHOW-显示当前数据库中所有表"
   },
   "SHOW_INDEX":{
       "desc":"SHOW-显示表的索引"
   },
   "SHOW_STATUS":{
       "desc":"SHOW-显示系统状态"
   },
   "SHOW_VARIABLES":{
       "desc":"SHOW-显示系统变量"
   },
   "SHOW_PROCESSLIST":{
       "desc":"SHOW-显示系统进程"
   },
   "SHOW_ENGINES":{
       "desc":"SHOW-显示系统存储引擎"
   },
   "SHOW_INNODB":{
       "desc":"SHOW-显示INNODB存储引擎"
   },
   "SHOW_LOGS":{
       "desc":"SHOW-显示存储引擎的日志"
   },
   "SHOW_WARNINGS":{
       "desc":"SHOW-显示警告"
   },
   "SHOW_ERRORS":{
       "desc":"SHOW-显示错误"
   }
     
}