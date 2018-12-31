# 트럼프 대통령의 1월 1~3일 트윗을 각각 리스트의 원소로 저장합니다.
trump_tweets = [
                'Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!',
                'Companies are giving big bonuses to their workers because of the Tax Cut Bill. Really great!',
                'MAKE AMERICA GREAT AGAIN!'
                ]

def date_tweet(tweet):
    '''
        트럼프 대통령의 트윗을 트윗 일자와 함께 출력합니다.
        '''
    
    # index에 0~2을 차례대로 저장하여 반복문을 실행합니다.
    for index in range(len(tweet)):
        print('2018년 1월 ' + str(index+1) + '일: ' + tweet[index])


# 실행 결과를 확인하기 위한 코드입니다.
date_tweet(trump_tweets)
