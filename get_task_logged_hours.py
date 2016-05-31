#!/usr/bin/python

__author__ = 'Shkodenko V. Taras'
import sys
 
total = len(sys.argv)
script_name = str(sys.argv[0])

if total < 2:
	print("Script usage: %s task_id " % script_name)
	exit(1)

task_id = int(sys.argv[1])

if not task_id:
	print('Error: task id should be greater than 0')
	exit(2)

from sqlite3 import connect

conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

curs.execute("select sum(w.hours), t.title from worklog w left join task_title t on t.task_id = w.task_id where w.task_id = %d" % task_id)
for row in curs:
	task_title = ''
	if row[1] is not None:
		task_title = row[1]
	print("Logged %s hours for task TS-%d %s" % (row[0], task_id, task_title))
