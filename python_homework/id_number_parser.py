def id_number_parser():
    id = input("주민등록번호 입력(-포함) : ")
    id = id.split("-")
    if id[1][0] == '1' or id[1][0] == '2':
        b_year = "19" + id[0][:2]
    else:
        b_year = "20" + id[0][:2]
    b_month = id[0][2:4]
    b_date = id[0][4:]
    print(f'{b_year}년 {b_month}월 {b_date}일')

id_number_parser()