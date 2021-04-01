from functions import to_int
from datetime import datetime

number = '13,451'


# print(type(to_int(number)))

date = '2021.3.29'
date_list = date.split('.')
print(date_list)
d = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
print(d)

now = datetime.now()
print(now)

elapse = (now-d).days
print(type(elapse))

print(int(1))
