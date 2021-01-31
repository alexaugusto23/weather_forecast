import time
for i in range(5):
   current_time = time.localtime()
   timestamp = time.strftime("%I:%m:%S", current_time)
   time.sleep(1)
   print(timestamp)