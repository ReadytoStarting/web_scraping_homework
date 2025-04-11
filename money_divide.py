def money_divide(money,people):
    dutch = money//people
    rest = money%people
    if rest !=0:
        print(f'각자 {dutch}원을 받고 {rest}원이 남습니다.')
    else:
        print(f'각자 {dutch}원을 받습니다.')

money_divide(10000,3)