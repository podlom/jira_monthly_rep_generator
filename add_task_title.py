#!/usr/bin/python

__author__ = 'Shkodenko V. Taras'
import sys
 
total = len(sys.argv)
script_name = str(sys.argv[0])

# print ("The total numbers of args passed to the script: %d " % total)
if total < 3:
	print("Script usage: %s task_id task_title" % script_name)
	exit(1)

task_id = int(sys.argv[1])
task_title = sys.argv[2]

if not task_id:
	print('Error: task id should be greater than 0')
	exit(2)

if not task_title:
	print('Error: task title can`t be empty')
	exit(3)

from sqlite3 import connect

conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

curs.execute("select title from task_title where task_id = %d" % task_id)
task_data = curs.fetchone()
if task_data == None:
	curs.execute("insert into task_title(task_id, title) values(%d, '%s')" % (task_id, task_title))
	conn.commit()
	print('Inserted data into task_title table set task_id: %d , task_title: %s' % (task_id, task_title))
else:
	print('task_title already have record with task_id: %d , task_title: %s' % (task_id, task_data[0]))
