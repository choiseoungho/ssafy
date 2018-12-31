# 트럼프 대통령의 트윗 세개로 구성된 리스트입니다. 수정하지 마세요.
trump_tweets = [
                "FAKE NEWS - A TOTAL POLITICAL WITCH HUNT!",
                "Any negative polls are fake news, just like the CNN, ABC, NBC polls in the election.",
                "The Fake News media is officially out of control.",
                ]

def lowercase_all_characters(text):
    '''
        리스트에 저장된 문자열을 모두 소문자로 변환합니다.
        
        >>> lowercase_all_characters(['FAKE NEWS', 'Fake News'])
        ['fake news', 'fake news']
        '''
    
    processed_text = []
    # 아래 코드를 작성하세요.
    for word in text:
        processed_text.append(word.lower())
    
    
    return processed_text


#아래 주석을 해제하고 결과를 확인해보세요.
print('\n'.join(lowercase_all_characters(trump_tweets)))
