import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'
pattern2 = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
password = 'hajsnkhn#4'


a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)