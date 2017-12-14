"""
获取每个章节的链接
"""

from bs4 import BeautifulSoup 
import requests

if __name__ == "__main__":
    server = "http://www.biqukan.com"
    target = "http://www.biqukan.com/28_28732/"
    req = requests.get(url = target)
    html = req.text
    div_bf = BeautifulSoup(html,"html.parser")
    div = div_bf.find_all("div",class_="listmain")
    print(div[0])
    a_bf = BeautifulSoup(str(div[0]),'html.parser')
    a = a_bf.find_all("a")

    f = open('result','w',encoding='utf-8')
    
    for each in a:
        f.write(each.string + server+each.get("href") + '\n')

    f.close()