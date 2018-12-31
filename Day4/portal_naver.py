'''
여러 포털 사이트의 인기 검색어
'''
# 다음 / 네이버 인기검색어 크롤링 함수 입니다.
keywords =[]
if "naver" in url:
    for data in soup.find_all("span",class_="ah_k"):
        if not data.get_text() in keywords:
            #10 위 까지만 크롤링 하겠습니다.
            if len(keywords)>=10:
                break
            keywords.append(data.get_text())
elif "daum" in url:
    for data in soup.find_all("a",class_="link_issue"):
        if not data.get_text() in keywords:
            keywords.append(data.get_text())

# Bugs 차트 Top 10 곡 제목
# 이제 내가 기획한 챗봇을 위한 함수를 구현해봅시다.
#예시) 네이버 영화 순위 크롤링
