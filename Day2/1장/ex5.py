# 트럼프 대통령 트윗을 공백 기준으로 분리한 리스트입니다. 수정하지 마세요.
trump_tweets = ['america', 'is', 'back', 'and', 'we', 'are', 'coming', 'back', 'bigger', 'and', 'better', 'and', 'stronger', 'than', 'ever', 'before']

def make_new_list(text):
    '''
        문자열로 구성된 리스트에서 b로 시작하는 모든 문자열을 새로운 리스트에 담습니다.
        '''
    
    # 아래 코드를 작성하세요.
    new_list =[]
    for word in text:
        if word.startswith('b') :
            new_list.append(word)
    
    
    return new_list


# 아래 주석을 해제하고 결과를 확인해보세요.
new_list = make_new_list(trump_tweets)
print(new_list)
