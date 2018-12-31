# 텍스트 파일을 불러옵니다.
filename = './corpus.txt'

def import_as_tuple(filename):
    tuples = []
    with open(filename) as file:
        for line in file:
            split = line.strip().split(',')
            word = split[0]
            freq = split[1]
            new_tuple = (word, freq)
            tuples.append(new_tuple)
    return tuples


# 아래 주석을 해제하고 결과를 확인해보세요.
print(import_as_tuple(filename))


# 아래 주석을 해제하고 결과를 확인해보세요.
# print(import_as_tuple(filename))
