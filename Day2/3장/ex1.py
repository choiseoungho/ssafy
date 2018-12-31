# 텍스트 파일을 불러옵니다.
source_file = "netflix.txt"

def make_dictionary(filename):
    '''
        텍스트 파일을 읽고 {'사용자 번호': '작품 번호'}로 구성된 딕셔너리를 리턴합니다.
        
        >>> make_dictionary(source_file)
        {'1': '1012', '2': '3781', ... }
        '''
    
    user_to_titles = {}
    with open(filename) as file:
        for line in file:
            # 아래 코드를 작성하세요.
            user, title = line.strip().split(':')
            user_to_titles[user] = title
        
        
        return user_to_titles


# 아래 주석을 해제하고 결과를 확인해보세요.
print(make_dictionary(source_file))
