from elice_utils import EliceUtils

elice_utils = EliceUtils()


def main():
    text_one = "나는 짜장면을 좋아합니다."
    text_list = text_one.split(" ")
    print (text_list)
    print(text_list[0])
    print(text_list[1])
    print(text_list[2].replace("좋아합니다.","안녕"))
    text_result = text_list[0] + text_list[1] + text_list[2]
    text_result2 = text_list[0]+" "+text_list[1]+" "+text_list[2].replace("좋아합니다.","안녕하세요")
    print(text_result2)
if __name__ == "__main__":
    main()
