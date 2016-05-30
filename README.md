# jira_monthly_rep_generator
Set of scripts which might be helpful to generate monthly report based on Jira tasks manager.

## Installation instructions

1. Set up SQLite3 DB. In this example I'm using /home/taras/my_scripts/wot.db
```
./wot_setup_db_table.py
```

2. Log worked hours to text file in this example stored in /home/taras/Documents/example_daily_tasks_report_month_year.txt
Each day log should be started from [ YYYY-MM-DD ]
Each entry should contain task URL and logged hours e.g.: https://jira.url/browse/TS-912 - 1h


3. At the end of the month import text file to DB using command:
```
./parse_example_report.py
```

4. Use different reports to get data:

4.1. Total number of worked hours by task in current month:
```
./get_current_year_month_total_work_hours.py
```

4.2. Total number of worked hour by task id:
```
./get_task_logged_hours.py task_id
```

4.3. Show tasks by date
```
./get_logged_work_by_date.py YYYY-MM-DD
```
