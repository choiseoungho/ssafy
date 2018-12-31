from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

elice_utils = EliceUtils()


def main():
    list = []
    list_content = []
    
    url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    
    for i in soup.find_all("div",class_="mfn_inner"):
        list.append("https://news.sbs.co.kr"+i.find("a")["href"])

    for i in range(0, len(list)):
        url = list[i]
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        
        list_content.append(soup.find("div",class_="text_area").get_text())

for i in list_content:
    
    if "KTX" in i:
        print("Okay")
        else:
            print("No")


if __name__ == "__main__":
    main()
