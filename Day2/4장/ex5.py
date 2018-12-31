# CSV 모듈을 임포트합니다.
import csv

def get_titles(books_csv):
    '''
        CSV 파일을 읽고 제목의 리스트를 리턴합니다.
        '''
    
    with open(books_csv) as books:
        reader = csv.reader(books, delimiter=',')
        # 함수를 완성하세요.
        get_title = lambda row: row[0]
        titles = map(get_title,reader)
        return list(titles)


# 작성한 코드를 테스트합니다. 주석을 해제하고 실행하세요.
books = 'books.csv'
titles = get_titles(books)
for title in titles:
    print(title)
