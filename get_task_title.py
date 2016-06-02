#!/usr/bin/python

__author__ = 'Shkodenko V. Taras'
import sys
 
total = len(sys.argv)
script_name = str(sys.argv[0])

if total < 2:
	print("Script usage: %s task_id " % script_name)
	exit()

task_id = int(sys.argv[1])

from sqlite3 import connect

conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

curs.execute("select title from task_title where task_id = %d" % task_id)
for row in curs:
	print("TS-%d %s" % (task_id, row[0]))
