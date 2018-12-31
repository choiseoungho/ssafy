# 단어어 해당 단어의 빈도수를 담은 리스트를 선언합니다. 수정하지 마세요.
pairs = [
         ('time', 8),
         ('the', 15),
         ('turbo', 1),
         ]

def get_freq(pair):
    '''
        (단어, 빈도수) 쌍으로 이루어진 튜플을 받아, 빈도수를 리턴합니다.
        
        >>> get_freq(('time', 8))
        8
        '''
    
    return pair[1]


def sort_by_frequency(pairs):
    '''
        (단어, 빈도수) 꼴 튜플의 리스트를 받아, 빈도수가 낮은 순서대로 정렬하여 리턴합니다.
        
        >>> sort_by_frequency(pairs)
        [('turbo', 1), ('time', 8), ('the', 15)]
        '''
    return sorted(pairs,key=get_freq)


# 아래 주석을 해제하고 결과를 확인해보세요.
print(sort_by_frequency(pairs))
