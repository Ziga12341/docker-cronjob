"""
Program create new file date.txt in repo.
In docker container you can find file in root folder
Every time (cron) call this script it write time in date.txt
"""
import datetime
f = open(f"date.txt", "a")
f.write(f"Time is: {datetime.datetime.now()} \n")
f.close()
