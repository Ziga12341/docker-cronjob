import datetime
f = open("date.txt", "a")
f.write(f"Time is: {datetime.datetime.now()}/n")
f.close()