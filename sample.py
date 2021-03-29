from logging import NOTSET
from functions import is_empty
items = [1, 2, 3, 4, 6]
print(len(items))

print(items[-1])
del items[1:len(items)]


print(items)
