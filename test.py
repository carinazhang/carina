import re
link = re.compile("\d+")
print(link)
content = "laowang-222haha"
info = re.sub(link,'www.cnpythoner.com',content)
print(info)
