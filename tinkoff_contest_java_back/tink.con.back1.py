import re
input_str = input()
result = re.sub('code\\d+','???', input_str)
print(result)
