
# encoding=UTF-8

import re

# re模块提供了不少有用的函数，用于匹配字符串，比如:
#     compile  该函数用户编译正则表达式，生成一个Pattern
#     match    该函数用户查找字符串的头部（也可以指定其实位置），它只匹配一次，只要找到一个匹配结果就返回，而不是查找全部匹配的结果
#     search   该函数用户查找字符串的头部（也可以指定其实位置），它只匹配一次，只要找到一个匹配结果就返回，而不是查找全部匹配的结果
#     findall  该函数匹配所有结果，findall 以列表形式返回全部能匹配的子串，如果没有匹配，则返回一个空列表。
#     finditer 该方法跟 findall 的行为类似，也是搜索整个字符串，获得所有匹配的结果。但它返回一个顺序访问每一个匹配结果（Match 对象）的迭代器。
#     split    该方法按照能够匹配的子串将字符串分割后返回列表
#     sub      该方法用于替换，
#     subn     subn 方法跟 sub 方法的行为类似，也用于替换

pattern = re.compile(r'\d+')

# 查找头部，没有匹配
m = pattern.match('one12twothree34four')
print(m)

m = pattern.match('one12twothree34four', 3, 10)
print(m)

# 这里如果使用 match 方法则不匹配
m = pattern.search('one12twothree34four')
print(m)
print(m.group())

# 查找数字全部的数字
m = pattern.findall('one12twothree34four')
print(m)

# finditer 方法的行为跟 findall 的行为类似，也是搜索整个字符串，获得所有匹配的结果。
# 但它返回一个顺序访问每一个匹配结果（Match 对象）的迭代器。
result_iter1 = pattern.finditer('hello 123456 789')
print(type(result_iter1))
for m1 in result_iter1:
    print('matching string: {}, position: {}'.format(m1.group(), m1.span()))

