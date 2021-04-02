import re
from datetime import datetime


def is_empty(value):
    return value == '' or value == [] or value == {} or value == None


def is_empty_obj(obj):
    if (not obj):
        return True

    # これ多分any型を使えばもっと綺麗にかける。
    for key in obj:
        if (is_empty(obj[key])):
            return True

    return False


def to_int(value):
    if (type(value) == int):
        return value

    return int(re.sub("\\D", "", value))


def get_elapsed_day_count(date):
    try:
        date_list = date.split('.')
        posted_date = datetime(int(date_list[0]), int(
            date_list[1]), int(date_list[2]))
        now = datetime.now()
        elapsed_day_count = (now-posted_date).days

        return elapsed_day_count
    except Exception as e:
        print(str(e))
        return None
