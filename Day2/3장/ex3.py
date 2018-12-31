# json 패키지를 임포트합니다.
import json

def create_dict(filename):
    '''
        JSON 파일을 읽고 문자열을 딕셔너리로 변환합니다.
        '''
    
    with open(filename) as file:
        json_string = file.read()
        # 함수를 완성하세요.
        return json.loads(json_string)


def create_json(dictionary, filename):
    '''
        JSON 파일을 읽고 딕셔너리를 JSON 형태의 문자열로 변환합니다.
        '''
    
    with open(filename, 'w') as file:
        # 함수를 완성하세요.
        json_string=json.dumps(dictionary)
        file.write(json_string)


# 아래 주석을 해제하고 결과를 확인해보세요.
src = 'netflix.json'
dst = 'new_netflix.json'

netflix_dict = create_dict(src)
#print('원래 데이터: ' + str(netflix_dict))

netflix_dict['Dark Knight'] = 39217
create_json(netflix_dict, dst)
updated_dict = create_dict(dst)
#print('수정된 데이터: ' + str(updated_dict))
