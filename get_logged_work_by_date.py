#!/usr/bin/python

__author__ = 'Shkodenko V. Taras'
import sys
 
total = len(sys.argv)
script_name = str(sys.argv[0])

if total < 2:
	print("Script usage: %s YYYY-MM-DD " % script_name)
	exit(1)

date = str(sys.argv[1])

import re

p = re.compile(r'\d{4}\-\d{2}\-\d{2}')
m = p.match(date)
if m:
	from sqlite3 import connect
	conn = connect(r'/home/taras/my_scripts/wot.db')
	curs = conn.cursor()
	curs.execute("select w.*, t.title from worklog w left join task_title t on t.task_id = w.task_id where w.date = '%s'" % date)
	for r1 in curs:
		(date, task_id, hours, title) = r1
		show_title = ''
		if title is not None:
			show_title = title
		print('Worked %d hours on TS-%d %s on %s' % (hours, task_id, show_title, date))
else:
	print('Error: invalid date provided: %s . Correct date should be in YYYY-MM-DD format.' % date)
	exit(2)
