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

curs.execute("select w.task_id, sum(w.hours), t.title from worklog w left join task_title t on t.task_id = w.task_id where w.date like '%s-%s%%' group by w.task_id" % (today_year, today_month))
for row in curs:
	(task_id, worked_hours, task_title) = row
	disp_title = ''
	if task_title is not None:
		disp_title = task_title
	print('%s %s\t%d' % (task_id, disp_title, worked_hours))
