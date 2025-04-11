import re
def email_validator():
    email = input("이메일을 입력하시오 : ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # if "@" in email and "." in email:
    if re.match(pattern, email):
        print('유효함')
    else:
        print('유효하지 않음')
    
email_validator()