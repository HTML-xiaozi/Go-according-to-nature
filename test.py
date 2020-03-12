import requests
import re
import os
import time

"""请求网页"""
respones = requests.get('https://www.vmgirls.com/12945.html')
html = respones.text
"""解析网页"""
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<a href="(.*?)" alt="你与晚霞同样浪漫" title="你与晚霞同样浪漫">',html)
print(urls)


"""保存图片"""
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    respones = requests.get(url)
    with open(dir_name + '/' + file_name,'wb') as f:
        f.write(respones.content)










