# matplotlib의 일부인 pyplot 라이브러리를 불러옵니다.
import matplotlib.pyplot as plt

# 엘리스에서 차트를 그릴 때 필요한 라이브러리를 불러옵니다.
from elice_utils import EliceUtils
elice_utils = EliceUtils()

# 월별 평균 기온을 선언합니다. 수정하지 마세요.
years = [2013, 2014, 2015, 2016, 2017]
temperatures = [5, 10, 15, 20, 17]

def draw_graph():
    '''
        막대 차트를 출력합니다.
        '''
    
    # 막대 그래프의 막대 위치를 결정하는 pos를 선언합니다.
    pos = range(len(years))  # [0, 1, 2, 3, 4]
    
    # 높이가 온도인 막대 그래프를 그립니다.
    # 각 막대를 가운데 정렬합니다.
    plt.bar(pos, temperatures, align='center')
    
    # 각 막대에 해당되는 연도를 표기합니다.
    plt.xticks(pos, years)
    
    # 그래프를 엘리스 플랫폼 상에 표시합니다.
    plt.savefig('graph.png')
    elice_utils.send_image('graph.png')

print('막대 차트를 출력합니다.')
draw_graph()
