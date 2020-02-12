#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
  
  
# 查询记录：
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from assets_tag')
# 获得查询结果集:
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()