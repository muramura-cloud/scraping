def is_empty(value):
    return value == '' or value == [] or value == {}


def to_int(value):
    value = value.replace(',', '')

    return int(value)
