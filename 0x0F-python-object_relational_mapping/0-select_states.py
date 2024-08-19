#!/usr/bin/python3
from MySQLdb import _mysql
import sys
arguments = sys.argv
print(_mysql.version_info)
db = _mysql.connect(host="localhost",user=arguments[0],password=arguments[1],database=arguments[2],port=3306)
db.query(""" SELECT * FROM states""")
r=db.store_result(maxrows='inf')
print(r.fetchRow())


