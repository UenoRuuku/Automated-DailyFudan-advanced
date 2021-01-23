import datetime
import threading
from dailyFudan import all

#i = 1

def func():
  #print("number " + str(i) + " run.")
  print("_____________daily run_____________")
  all()
  print("______________success______________")
  #i += 1
  timer = threading.Timer(86400, func)
  timer.start()
 

now_time = datetime.datetime.now()

next_time = now_time + datetime.timedelta(days=+1)
next_year = next_time.date().year
next_month = next_time.date().month
next_day = next_time.date().day

next_time = datetime.datetime.strptime(str(next_year)+"-"+str(next_month)+"-"+str(next_day)+" 03:00:00", "%Y-%m-%d %H:%M:%S")

# last_time = now_time + datetime.timedelta(days=-1)
 

timer_start_time = (next_time - now_time).total_seconds()
print("start running at " + str(timer_start_time))
# 54186.75975
print("test running")
all()
print("success")
timer = threading.Timer(timer_start_time, func)
timer.start()