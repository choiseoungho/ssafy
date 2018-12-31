from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

elice_utils = EliceUtils()


def main():
    print("최신 뉴스 기사 href 수집")
    
    # href 수집할 사이트 주소 입력
    url = "https://news.nate.com/recent?mid=n0100"
    
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    
    # 1. a 태그가 있는 div 태그 및 class 찾기
    # 2. find("a")["href"]로 href 추출
    list_href=[]
    for href in soup.find_all("div",class_="mduSubjectList"):
        list_href.append("https://news.nate.com/recent?mid=n0100"+href.find("a")["href"])
    print(list_href)


if __name__ == "__main__":
    main()
