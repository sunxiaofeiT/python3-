# coding = utf-8
# author: sunpengfei
# python 3.6
# filename: daomubiji1
# desc: 下载盗墓笔记1，txt
# 支持正版小说，代码仅供交流

import sys

import requests
from bs4 import BeautifulSoup

target_url = "http://www.daomubiji.com/"

home_req = requests.get(target_url)
home_html = home_req.text
home_div = BeautifulSoup(home_html,"html.parser")
home_a_down = home_div.find_all("a")
home_as = []
for each_a in home_a_down[2:13]:
	home_as.append(each_a.get("href"))

# print(home_as)

names = []  # 章节名字
urls = []  # 章节链接
nums = 0  # 每部章节数

for each_url in home_as:
	req = requests.get(each_url)
	html = req.text

	div_bf = BeautifulSoup(html, "html.parser")
	div = div_bf.find_all("article", class_="excerpt excerpt-c3")

	nums = len(div)

	for each in div:
		a_bf = BeautifulSoup(str(each), "html.parser")
		a = a_bf.find_all("a")
		for each in a:
			names.append(each.string)
			urls.append(each.get("href"))

all_nums = len(urls)	# 总的章节数

def writer(name, path, text):
    write_flag = True
    with open(path, "a", encoding="utf-8") as f:
        f.write(name + "\n")
        f.write(text)
        f.write("\n\n")


print("盗墓笔记开始下载-------------")

for i in range(all_nums):
	each_req = requests.get(urls[i])
	each_html = each_req.text
	# each_html = each_html.decode("utf-8")
	each_bf = BeautifulSoup(each_html, "html.parser")
	each_content = each_bf.find_all("article", class_="article-content")
	each_text = each_content[0].text
	# print(each_bf)
	# print(each_text)
	# each_text = each_content.text.replace("\xa0"*8,"\n\n")
	writer(names[i], "盗墓笔记.txt", each_text)
	sys.stdout.write("已下载： %.1f" % float((i / all_nums) * 100) + "% \r")
	sys.stdout.flush()
