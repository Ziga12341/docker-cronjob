"""
Program creates new file date.txt
The file is located in /root/date.txt in Docker container (because of default work directory).
On every cron execution this script adds time entry in date.txt
"""
import datetime
f = open(f"date.txt", "a")
f.write(f"Time is: {datetime.datetime.now()} \n")
f.close()
