import csv
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from operator import itemgetter

from elice_utils import EliceUtils
elice_utils = EliceUtils()

### json에서 원래 키는 큰 따옴표로 나누어져 있어야 되는데
## 키가 작은 따옴표로 나누어져 있다.-> 이건 올바른 형식은 아닌거
### 따라서 작은 따옴표를 큰 따옴표를 미리 만들어 놓은 것
def jsonify(data):
    return json.loads(data.replace("'", '"'))


def preprocess_talks(src):
    '''
        주어진 CSV 파일을 열어 처리 가능한 파이썬의 리스트 형태로 변환합니다.
        리스트의 각 원소는 문제에서 설명된 딕셔너리 형태로 이루어져 있습니다.
        
        각 강연 별로 다음과 같은 키와 타입을 가진 딕셔너리를 생성합니다:
        {
        "title": string,
        "speaker": string,
        "views": int,
        "comments": int,
        "duration": int,
        "languages": int,
        "tags": list(string),
        "ratings": list(dict)
        }
        
        >>> preprocess_talks('ted.csv')
        [{'title': 'Do schools kill creativity?', 'speaker': 'Ken Robinson', ... }]
        '''
    
    # 강연 데이터를 저장할 빈 리스트를 선언합니다.
    talks = []
    
    # CSV 파일을 열고, 데이터를 읽어 와서 talks에 저장합니다.
    with open(src) as talks_file:
        reader = csv.reader(talks_file,delimiter=',')
        #여기서 각 열로 무엇으로 나누어져있는지 확인해보
        for row in reader:
            try:
                talk = {
                    'title': row[14],     # 강연의 제목
                    'speaker': row[6],   # 강연자의 이름
                    'views': int(row[16]),     # 조회수
                    'comments': int(row[0]),  # 댓글의 개수
                    'duration': int(row[2]),  # 강연 길이
                    'languages': int(row[5]), # 지원하는 언어의 수
                    'tags': jsonify(row[13]),  # 관련 태그 (키워드)
                    'ratings': jsonify(row[10]),   # 강의에 대한 평가
            }
            except:
                pass
            talks.append(talk)
#Try except 설명 해 야됨...
return talks


### 가장 인기 있는 태그 상위 n개를 리턴하는 함수
def get_popular_tags(talks, n):
    '''
        가장 인기 있는 태그 상위 n개를 리턴합니다.
        태그의 인기도는 해당 태그를 포함하는 강의들의 조회수 합으로 결정됩니다.
        예를 들어, 'education' 태그가 포함된 강의가 총 15개라면
        'education' 태그의 인기도는 이 15개 강의의 조회수 총합입니다.
        
        >>> get_popular_tags(preprocess_talks('ted.csv'), 10))
        ['culture', 'technology', 'science', ... ]
        '''
    # 태그 별 인기도를 저장할 딕셔너리
    tag_to_views = {}
    
    # 태그 별 인기도를 구해 tag_to_views에 저장합니다.
    for talk in talks:
        tags = talk['tags']
        views = talk['views']
        print(tags)
        for tag in tags:
            if tag in tag_to_views:
                tag_to_views[tag] += views
            else:
                tag_to_views[tag] = views
    tag_view_pairs = list(tag_to_views.items())
    #딕셔러니에서 내가 원하는 것을 찾아 올때는 시간이 걸림.
    #키 는 테그 values 인기도 인 딕셔러니
    # (태그, 인기도)의 리스트 형식으로 변환합니다.
    # 태그의 수만큼 리스트 준다.
    # 인기도가 높은 순서로 정렬해 앞의 n개를 취합니다.
    # n개를 취한 후에는 태그만 남깁니다.
    # 힌트: itemgetter()를 사용하세요!
    # 여기 잘 말해줘야 됨~
# tag_view_pair = ("education',1000")
# get_tag_name(pair)=> 'education'
# get_popluarity = itemgetter(1)
# get_popluarity(pair) => 1000

top_tag_and_views = sorted(tag_view_pairs, key=itemgetter(1), reverse=True)[:n]
    ## tuple에서 itemgetter 0 들어가는 거 한번 물어보고
    # tuple 에서 태그 얻는 것 0 -> tuple 에서 아이템 얻는 것은 1
    ## map 함수는 특정한 함수 리스트 취해주는 함수
    #함수 , 리스트
    top_tags = map(itemgetter(0),top_tag_and_views)
    # 두번째는 머 들어가야 되는지 물어보기
    # Map 함수를 꼭 알아야 된다고 언급
    # nubmers = [1,2,3]  -> [-1,-2,-3] 이렇게
    # negative nubmers = map(lambda x: -x, numbers)
    return list(top_tags)

# 그다음에 3개 함수 들어갈 입력 작성한다고 언급
def completion_rate_by_duration(talks):
    '''
        강의 길이에 따라 강의를 끝까지 들은 비율(완수도)이 어떻게 변화하는지 확인해 봅니다.
        강의를 끝까지 들은 비율은 (댓글 개수 / 조회수)에 비례한다고 가정합니다.
        '''
    #한줄 짜리 코드를 만드는데 list comprehension을 사용
    durations = [talk['duration'] for talk in talks] # talks의원소가머가 들어갈건지
    completion_rates = [talk['comments']/talk['views'] for talk in talks]
    scatter_plot(durations, completion_rates, '강의 길이', '완수도')
    
    return durations, completion_rates


def views_by_languages(talks):
    '''
        지원되는 언어의 수에 따라 조회수가 어떻게 변화하는지 확인해 봅니다.
        '''
    languages = [talk['languages'] for talk in talks]
    views = [talk['views'] for talk in talks]
    scatter_plot(languages, views, '언어의 수', '조회수')
    
    # 채점을 위해 결과를 리턴합니다.
    return views, languages


def show_ratings(talk):
    '''
        강의에 대한 다양한 평가(rating)를 막대그래프로 표현합니다.
        각 키워드('fun', 'confusing' 등)별 숫자를 나타냅니다.
        '''
    ratings = talk['ratings']
    keywords = [rating['name'] for rating in ratings]
    #문자열의 키는 name
    counts = [rating['count'] for rating in ratings]
    #ratings 는 딕셔너리
    #딕셔너리는 키 아이디 있엇는데
    #키워드 와 카운드를 얻는 막대그래프가 의미하는 것
    bar_plot(keywords, counts, '키워드', 'rating의 수')
    
    # 채점을 위해 결과를 리턴합니다.
    return keywords, counts


def scatter_plot(x, y, x_label, y_label):
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    plt.scatter(x, y)
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    
    plt.xlim((min(x), max(x)))
    plt.ylim((min(y), max(y)))
    plt.tight_layout()
    
    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)


def bar_plot(x_ticks, y, x_label, y_label):
    assert(len(x_ticks) == len(y))
    
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    pos = range(len(y))
    plt.bar(pos, y, align='center')
    plt.xticks(pos, x_ticks, rotation='vertical', fontproperties=font)
    
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    plt.tight_layout()
    
    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)

### 함수가 7개 중 2개는 미리 작성이 되어 있고 추가적으로 하나의 함수를 준비함.
def main():
    src = 'ted.csv'
    talks = preprocess_talks(src)
    print(get_popular_tags(talks, 10))
    completion_rate_by_duration(talks)
    views_by_languages(talks)
    show_ratings(talks[0])


if __name__ == "__main__":
    main()

