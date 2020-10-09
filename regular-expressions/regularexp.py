import re

pattern = re.compile('this')
pattern2 = re.compile('search this inside of this text, please!')
pattern3 = re.compile(r"([a-zA-Z]).([a])")
string = 'search this inside of this text, please! Paty'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern2.match(string)
e = pattern3.search(string)

print(a.span())
print(a.start())
print(a.group())
print(a.end())
print(b)
print(c)
print(d)
print(e.group())

