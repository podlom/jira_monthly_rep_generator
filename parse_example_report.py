#!/usr/bin/env python

__author__ = 'Shkodenko V. Taras'

from sqlite3 import connect
conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

import re

file_lines = []
with open("/home/taras/Documents/example_daily_tasks_report_month_year.txt", "r") as f:
	for line in f:
		file_lines.append(line.rstrip('\n').rstrip('\r'))

for line1 in file_lines:
	# print line1
	p = re.compile(r'\[ (\d{4}\-\d{2}\-\d{2}) \]')
	m = p.match(line1)
	if m:
		# print 'Match found: ', m.groups()
		date = m.group(1)
		# print 'Set current date to: ', date
	# else:
		# print 'Not a date line'
	p1 = re.compile(r'https://jira.url/browse/TS\-(\d+) - (\d+)h')
	m1 = p1.match(line1)
	if m1:
		task_id = int(m1.group(1))
		log_hrs = int(m1.group(2))
		print 'Worked on task YS-', task_id ,' ', log_hrs ,' hours on ', date
		curs.execute("select * from worklog where date = '%s' and task_id = %d and hours = %d" % (date, task_id, log_hrs))
		log_data = curs.fetchone()
		if log_data == None:
			print 'Need to insert data'
			curs.execute("insert into worklog(date, task_id, hours) values('%s', %d, %d)" % (date, task_id, log_hrs))
			conn.commit()
			#
			curs.execute("select * from worklog where date = '%s' and task_id = %d and hours = %d" % (date, task_id, log_hrs))
			log_data1 = curs.fetchone()
			if log_data1 != None:
				print 'Inserted data to log'
