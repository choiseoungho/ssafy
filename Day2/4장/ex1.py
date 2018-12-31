# csv 모듈을 임포트합니다.
import csv

def print_book_info(filename):
    '''
        CSV에서 제목, 저자, 페이지를 추출합니다.
        '''
    
    # 아래 주석을 해제하고 실행 결과를 확인해보세요.
    with open(filename) as file:
        # ',' 기호로 분리된 CSV 파일을 처리하세요..
        reader = csv.reader(file,delimiter=',')
        
        # 처리된 파일의 각 줄을 불러옵니다.
        for row in reader:
            # 함수를 완성하세요.
            title = row[0]
            author = row[1]
            pages = row[3]
            print("{} ({}): {}p".format(title, author, pages))


# 아래 주석을 해제하고 실행 결과를 확인해보세요.
filename = 'books.csv'
print_book_info(filename)
