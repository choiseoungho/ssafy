# 크롤링 함수입니다.
def _crawl_naver_keywords(text):
    url = re.search(r'(https?://\S+)',text.split('|')[0]).group(0)
    req = urllib.request.Request(url)
    sourcecode = urlib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode,"html.parser")

    keywords=[]
    #enumerate 란 "열거하다"라는 뜻
    #이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
    #인덱스 값을 포함하는 enumerate 객체를 리턴한다.
    '''
    example:
    for i,name in enumerate(['body','foo','bar']):
        print(i,name)
    #result
    0 body
    1 foo
    2 bar
    '''
    #장점 for 문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
    for i, keyword in enumerate(soup.find_all("span",class_="ah_k")):
        if i< 20:
            keywords.append(keyword.get_text())
    #한글 지원을 위해 앞에 unicode u를 붙혀준다.
    return u'\n'.join(keywords)
