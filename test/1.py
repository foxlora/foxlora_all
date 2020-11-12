import re
text = open('C:\\Users\\18351\\Desktop\\export.txt',mode='r')
content = text.read()
text.close()

sysname_pattern = re.compile(r'<(.*?)>\s*sys')
sysname_res = sysname_pattern.findall(content)
print(sysname_res)