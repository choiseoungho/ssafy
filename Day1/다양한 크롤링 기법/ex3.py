from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

elice_utils = EliceUtils()


def main():
    list_href = []
    list_content = []
    
    url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    
    for href in soup.find_all("div",class_="mfn_inner"):
        list_href.append("https://news.sbs.co.kr"+href.find("a")["href"])

    for i in range(0, len(list_href)):
        url = list_href[i]
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        
        list_content.append(soup.find("div",class_="text_area").get_text())

print(list_href)
print(list_content)


if __name__ == "__main__":
    main()
