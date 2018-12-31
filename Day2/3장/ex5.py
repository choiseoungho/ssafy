# 각 영화 별 시청자 리스트를 임포트합니다.
from viewers import dark_knight, iron_man

dark_knight_set = set(dark_knight)
iron_man_set = set(iron_man)

# 두 작품을 모두 시청한 사람의 수
both = len(dark_knight_set & iron_man_set)

# 두 작품 중 최소 하나를 시청한 사람의 수
either = len(dark_knight_set | iron_man_set)

# 다크나이트만 시청한 사람의 수
dark_knight_only = len(dark_knight_set - iron_man_set)

# 아이언맨만 시청한 사람의 수
iron_man_only = len(iron_man_set - dark_knight_set)


# 아래 주석을 해제하고 실행 결과를 확인해보세요.
print("두 작품 모두 시청: {}명".format(both))
print("하나 이상 시청: {}명".format(either))
print("다크나이트만 시청: {}명".format(dark_knight_only))
print("아이언맨만 시청: {}명".format(iron_man_only))
