#!/usr/bin/env python
#-*-conding:utf-8-*-
import pymysql

from  sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:jia@1234@172.21.129.252:3306/s11", max_overflow=5)

engine.execute(
    "INSERT INTO ts_test (a, b) VALUES ('2', 'v1')"
)

engine.execute(
     "INSERT INTO ts_test (a, b) VALUES (%s, %s)",
    ((555, "v1"),(666, "v1"),)
)
engine.execute(
    "INSERT INTO ts_test (a, b) VALUES (%(id)s, %(name)s)",
    id=999, name="v1"
)

result = engine.execute('select * from ts_test')
result.fetchall()
