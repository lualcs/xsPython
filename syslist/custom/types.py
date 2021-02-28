# file:type.py.py
# desc:类型判断
# auth:Carol Luo
# date:2021/2/24 23:14
#整数
def is_int(v: any):
    return isinstance(v, int)

#小数
def is_float(v: any):
    return isinstance(v, float)

#复数
def is_complex(v: any):
    return isinstance(v, complex)

#布尔
def is_bool(v: any):
    return isinstance(v, bool)

#列表
def is_list(v: any):
    return isinstance(v, list)

#元组
def is_tuple(v: any):
    return isinstance(v, tuple)

#集合
def is_set(v: any):
    return isinstance(v, set)

#字典
def is_map(v: any):
    return isinstance(v, dict)

#符串
def is_string(v: any):
    return isinstance(v, str)




