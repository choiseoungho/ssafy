# 트럼프 대통령의 트윗으로 구성된 문자열입니다. 수정하지 마세요.
trump_tweets = "thank you to president moon of south korea for the beautiful welcoming ceremony it will always be remembered"

def break_into_words(text):
    '''
        공백 기준으로 분리된 문자열을 리스트형으로 반환합니다.
        
        >>> break_into_words('merry christmas')
        ['merry', 'christmas']
        '''
    
    # 아래 코드를 작성하세요.
    words = text.split()
    
    
    return words


# 아래 주석을 해제하고 결과를 확인해보세요.
print(break_into_words(trump_tweets))
