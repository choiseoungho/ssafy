# 단어 모음을 선언합니다. 수정하지 마세요.
words = [
         'apple',
         'banana',
         'alpha',
         'bravo',
         'cherry',
         'charlie',
         ]

def filter_by_prefix(words, prefix):
    '''
        prefix로 시작하는 word를 린턴합니다.
        
        >>> filter_by_prefix(words, 'a')
        'apple'
        '''
    return [word for word in words if word.startswith(prefix)]


# 아래 주석을 해제하고 결과를 확인해보세요.
a_words = filter_by_prefix(words, 'a')
print(a_words)
