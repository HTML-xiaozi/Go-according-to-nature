import requests
import re
import os
import time

"""请求网页"""
respones = requests.get('URL')
html = respones.text
"""解析网页"""
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<a href="(.*?)" alt="" title="">',html)
print(urls)


"""保存图片"""
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    respones = requests.get(url)
    with open(dir_name + '/' + file_name,'wb') as f:
        f.write(respones.content)










