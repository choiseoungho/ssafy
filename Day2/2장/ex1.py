# 텍스트 파일을 불러옵니다.
corpus = 'corpus.txt'

def print_lines(filename):
    '''
        파일의 내용을 줄 번호와 한 줄씩 출력합니다.
        
        >>> print_lines(corpus)
        1 zoo,768
        2 zones,1168
        3 zone,2553
        '''
    line_number = 1
    # 아래 코드를 작성하세요.
    with open(filename) as file:
        for line in file:
            print(str(line_number) + ' '+ line)
            line_number += 1


# 아래 주석을 해제하고 결과를 확인해보세요.
print_lines(corpus)
