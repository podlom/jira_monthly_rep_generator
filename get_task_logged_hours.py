#!/usr/bin/python

__author__ = 'Shkodenko V. Taras'
import sys
 
total = len(sys.argv)
script_name = str(sys.argv[0])

# print ("The total numbers of args passed to the script: %d " % total)
if total < 2:
	print("Script usage: %s task_id " % script_name)
	exit()

task_id = int(sys.argv[1])

from sqlite3 import connect

conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

curs.execute("select sum(hours) from worklog where task_id = %d" % task_id)
# print curs.fetchall()
for row in curs:
	print("Logged %s hours for task YS-%d" % (row[0], task_id))
