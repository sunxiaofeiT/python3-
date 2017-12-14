from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = "http://www.biqukan.com/28_28732/10500101.html"
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all("div",class_="showtxt")
    print(texts[0].text.replace('\xa0'*8,'\n\n'))
