# file:type.py.py
# desc:类型判断
# auth:Carol Luo
# date:2021/2/24 23:14

def is_int(v: any):
    return isinstance(v, int)


def is_float(v: any):
    return isinstance(v, float)


def is_complex(v: any):
    return isinstance(v, complex)


def is_bool(v: any):
    return isinstance(v, bool)


def is_list(v: any):
    return isinstance(v, list)


def is_tuple(v: any):
    return isinstance(v, tuple)


def is_set(v: any):
    return isinstance(v, set)


def is_map(v: any):
    return isinstance(v, dict)


def is_string(v: any):
    return isinstance(v, str)




