#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
这个示例文件展示了如何在Python代码中使用SQL高亮功能。
支持自动检测SQL代码，无需添加显式标记。
"""

import sqlite3
import pandas as pd

# 连接到SQLite数据库
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 创建表格
create_table_query = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
cursor.execute(create_table_query)

# 插入数据
insert_data_query = '''
INSERT INTO users (name, email, age) VALUES
    ('张三', 'zhangsan@example.com', 25),
    ('李四', 'lisi@example.com', 30),
    ('王五', 'wangwu@example.com', 22);
'''
cursor.execute(insert_data_query)
conn.commit()

# 查询数据
def get_users_by_age(min_age):
    query = f"""
    SELECT 
        id,
        name,
        email,
        age
    FROM 
        users
    WHERE 
        age >= {min_age}
    ORDER BY 
        age DESC;
    """
    return pd.read_sql_query(query, conn)

# 使用查询函数
users = get_users_by_age(25)
print(users)

# 关闭连接
conn.close()
