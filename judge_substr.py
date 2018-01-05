#coding=utf-8
#__author__ = 'chenyuanyuan'
#判断字符串
str_a = "你好"
str_b = "你好小明同学，欢迎你的到来"


def is_sub_str(sub_strs, strs):
    """
    判断sub_strs是否为strs的子串
    :param sub_strs：子串
    :param strs：父串
    :return True/False
    """
    if sub_strs in strs:
        return True
    else:
        return False

def is_move_str(str_a, str_b):
    """判断一个串是否为另一个串通过循环右移n位产生的子串
    :param sub_strs：子串
    :param strs：父串
    :return True/False
    """
    b_len = len(str_b)
    for i in range(b_len):
        move_str = str_b[-i:]+str_b[:-i]
        print(is_sub_str(str_a, move_str))
    return False

a = is_sub_str(str_a, str_b)
print(a)

b = is_move_str(str_a, str_b)
print(b)
