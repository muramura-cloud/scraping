def is_empty(value):
    return value == '' or value == [] or value == {} or value == None


def is_empty_obj(obj):
    if (not obj):
        return True

    for key in obj:
        if (is_empty(obj[key])):
            return True

    return False


def to_int(value):
    return int(value.replace(',', ''))
