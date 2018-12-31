# 트럼프 대통령의 트윗 세개로 구성된 리스트입니다. 수정하지 마세요.
trump_tweets = [
                "i hope everyone is having a great christmas, then tomorrow it’s back to work in order to make america great again.",
                "7 of 10 americans prefer 'merry christmas' over 'happy holidays'.",
                "merry christmas!!!",
                ]

def remove_special_characters(text):
    '''
        리스트에 저장된 문자열에서 쉼표, 작은따옴표, 느낌표를 제거합니다.
        
        >>> remove_special_characters(["wow!", "wall,", "liberals'"])
        ['wow', 'wall', 'liberals']
        '''
    
    processed_text = []
    # 아래 코드를 작성하세요.
    for sentence in text:
        sentence = sentence.replace(",","").replace("'","").replace("!","")
        processed_text.append(sentence)
    
    
    return processed_text


#아래 주석을 해제하고 결과를 확인해보세요.
print('\n'.join(remove_special_characters(trump_tweets)))
