# datetime to be able to timestamp logs
import datetime

now = datetime.datetime.now()

#2017-10-25 08:45:31.941473
print(now)

#8-45-25-10-2017
string_now = '{}-{}-{}-{}-{}'.format(now.hour, now.minute, now.day, now.month, now.year)
print(string_now)

#2017/10/25 08:45:31
print(now.strftime('%Y/%m/%d %H:%M:%S'))

# create a log file with a timestamp in the name
# log-file-2017-10-25-08-50-27
string_now_time = now.strftime('%Y-%m-%d-%H-%M-%S')
log = 'log-file-' + string_now_time

with open(log, 'w') as file:
    file.write(string_now_time)
    file.close()
