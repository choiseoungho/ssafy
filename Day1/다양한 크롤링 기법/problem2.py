from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

elice_utils = EliceUtils()


def main():
    print("최신 뉴스 기사 href 안의 내용 수집")
    
    # href 수집할 사이트 주소 입력
    url = "https://news.nate.com/recent?mid=n0100"
    
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
        
        # 1. a 태그가 있는 div 태그 및 class 찾기
        # 2. find("a")["href"]로 href 추출
        print("href 출력해보기")
    
    list_href = []

    # 반복문을 사용해 원하는 정보 range(3,23)까지 find("a")["href"] 를 사용해서
    # href 모두 수집하여 list_href에 저장

for i in range(3,23):
    list_href.append(soup.find_all("span",class_="tit")[i].find("a")["href"])
    # 3. 문자열 http: 를 앞에 추가해줌으로써 완벽한 링크 만들기
    # 4. list에 넣기
    
    links = []
    
    for i in -:
        links.append(-)

    # 1. list의 크기 만큼 for 루프 출력
    # 2. url에 list에 있는 href 링크 하나씩 넣어서 출력하기

    for i in -:
        url = -
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        
        print(soup)


if __name__ == "__main__":
    main()
