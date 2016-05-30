#!/usr/bin/env python

__author__ = 'Shkodenko V. Taras'

import commands
from sqlite3 import connect
from datetime import date

today = date.today()
today_month = today.strftime('%m')
today_year = today.strftime('%Y')

conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

curs.execute("select task_id, sum(hours) from worklog where date like '%s-%s%%' group by task_id" % (today_year, today_month))
# print curs.fetchall()
for row in curs:
	# print(row)
	(task_id, worked_hours) = row
	print('%s\t%d' % (task_id, worked_hours))	
