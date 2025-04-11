

# def time_converter(second):
#     print(f'{second}초는 ',end="")
#     hour = second//3600
#     second = second %3600
#     if hour!=0:
#         print(f'{hour}시간 ',end="")
#     minute = second//60
#     if minute!=0:
#         print(f'{minute}분 ',end="")
#     second = second%60
#     if second!=0:
#         print(f'{second}초입니다.')
#     else:
#         print("입니다.")

# time_converter(14040)

def time_converter(second):
    print(f'{second}초는 ')
    hour, second = divmod(second, 3600)
    minute, second = divmod(second, 60)

    result = []
    if hour:
        result.append(f"{hour}시간")
    if minute:
        result.append(f"{minute}분")
    if second:
        result.append(f"{second}초")

    print(f"{' '.join(result)}입니다.")

time_converter(12345)