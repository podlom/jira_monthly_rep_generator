#!/usr/bin/python

__author__ = 'Shkodenko V. Taras'

from sqlite3 import connect
conn = connect(r'/home/taras/my_scripts/wot.db')
curs = conn.cursor()

curs.execute('create table worklog(date, task_id, hours)')
